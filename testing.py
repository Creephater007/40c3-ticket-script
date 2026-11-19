from playwright.sync_api import sync_playwright
import time
import sys
from datetime import datetime, timedelta

TARGET_TIME = datetime.now() + timedelta(seconds=30)  # Set the target time to 30 seconds from now
URL = "https://tickets.events.ccc.de/"

print(f"Waiting until {TARGET_TIME} to open the ticket shop...")

def main():
    with sync_playwright() as p:

        # Launch a visible Chromium browser
        browser = p.chromium.launch(
            headless=False,
            slow_mo=0
        )

        try:
            page = browser.new_page()

            time.sleep((TARGET_TIME - datetime.now()).total_seconds())  # Wait until the specified time
            
            while True:
                try:
                    # Navigate to the ticket shop
                    page.goto(URL)

                    # Wait for the page to load
                    page.wait_for_load_state("domcontentloaded")

                    # Read visible text from the page
                    page_text = page.locator("body").inner_text().lower()

                    # Check for nginx error
                    if "nginx" in page_text and "500" in page_text:
                        print("[ERROR] nginx 500 detected!")
                        continue

                    print("[SUCCESS] Ticket shop opened!")
                    print("Current URL:", page.url)

                    break  # Exit the loop if successful

                except Exception as e:
                    print(f"[EXCEPTION] {e}")
                    time.sleep(1)  # Wait before retrying

            # Keep browser open
            print("[INFO] Browser is open.")

            try:
                if sys.stdin.isatty():
                    input("Press Enter to close the browser...")
                else:
                    raise EOFError

            except EOFError:
                print("[INFO] No interactive input available.")
                print("[INFO] Close the browser window manually to exit.")

                # Wait until browser is manually closed
                while browser.is_connected():
                    time.sleep(0.5)

        except KeyboardInterrupt:
            print("\n[INFO] Interrupted by user.")

        finally:
            if browser.is_connected():
                browser.close()

            print("[INFO] Browser closed.")


if __name__ == "__main__":
    main()
