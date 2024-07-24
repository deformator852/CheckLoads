from playwright.sync_api import sync_playwright
from haully import Haully  # pyright:ignore
import config
import threading
import time

def main():
    stop_event = threading.Event()

    def run_haully(playwright):
        browser = playwright.firefox.launch(headless=False)
        context = browser.new_context(
            user_agent=config.USER_AGENT, viewport={"width": 1920, "height": 1080}
        )
        page = context.new_page()
        driver = page
        haully = Haully(driver)
        while True:
            try:
                haully.start("https://www.haully.com/")
            except Exception as e:
                print(e)
            time.sleep(300)
        # stop_event.set()
        # browser.close()

    with sync_playwright() as playwright:
        run_haully(playwright)


if __name__ == "__main__":
    main()
