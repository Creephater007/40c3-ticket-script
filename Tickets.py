from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
import time

# ---------------- CONFIGURATION ----------------

URL = "https://tickets.events.ccc.de/"

# Delay between failed attempts (seconds).
# Avoid sending requests continuously to the server.
RETRY_DELAY = 2

NAVIGATION_TIMEOUT = 15000

# ------------------------------------------------


def is_nginx_error(page, response):
    """Check whether the main page returned an nginx 500 error."""

    if response is None:
        return False

    #if response.status != 500:
    #    return False

    try:
        body = page.locator("body").inner_text(timeout=5000).lower()

        return (
            "nginx" in body
            or "500" in body
        )

    except Exception:
        return False


def main():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False,
            slow_mo=0
        )

        page = browser.new_page()

        page.set_default_navigation_timeout(NAVIGATION_TIMEOUT)

        # Event listener: monitor main document responses
        def on_response(response):

            request = response.request

            if (
                request.is_navigation_request()
                and request.frame == page.main_frame
            ):
                print(
                    f"[HTTP] {response.status} - {response.url}"
                )

        page.on("response", on_response)

        print(f"Opening ticket shop: {URL}")

        while True:

            try:
                # Initial navigation or subsequent reload
                response = page.goto(
                    URL,
                    wait_until="domcontentloaded"
                )

                if is_nginx_error(page, response):

                    print("[ERROR] nginx 500 detected!")
                    #print(f"Retrying in {RETRY_DELAY} seconds...")

                    #time.sleep(RETRY_DELAY)
                    continue

                print("[SUCCESS] nginx error not detected!")
                print("Current URL:", page.url)

                break

            except PlaywrightTimeoutError:
                print("[TIMEOUT] Navigation timed out. Retrying...")
                time.sleep(RETRY_DELAY)

            except Exception as error:
                print("[ERROR]", error)
                time.sleep(RETRY_DELAY)

        print("Browser is ready. Automation finished.")

        input("Press Enter to close the browser...")

        browser.close()


if __name__ == "__main__":
    main()
