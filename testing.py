from playwright.sync_api import sync_playwright
import time
from datetime import datetime, timedelta

TARGET_TIME = datetime.now() + timedelta(seconds=10)  # Set the target time to 10 seconds from now
print(f"Waiting until {TARGET_TIME} to open the ticket shop...")

def main():
    with sync_playwright() as p:

        # Launch a visible Chromium browser
        browser = p.chromium.launch(
            headless=False,
            slow_mo=0
        )

        # Create a new browser tab
        page = browser.new_page()

        time.sleep((TARGET_TIME - datetime.now()).total_seconds())  # Wait until the specified time

        while True:
            try:
                # Navigate to the ticket shop
                page.goto("https://tickets.events.ccc.de/")

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

        # Keep the browser open until manually closed
        input("Press Enter to close the browser...")

        browser.close()


if __name__ == "__main__":
    main()
