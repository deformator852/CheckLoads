from playwright.sync_api import sync_playwright
from haully import Haully  # pyright:ignore
import config
import threading
import time

def main():
    #stop_event = threading.Event()

    def run_browser():
        stop_event = threading.Event()
        browser = playwright.firefox.launch(headless=True)
        context = browser.new_context(
            user_agent=config.USER_AGENT, viewport={"width": 1920, "height": 1080}
        )
        page = context.new_page()
        driver = page
        haully = Haully(driver)
        try:
            haully.start("https://www.haully.com/")
        except Exception as e:
            print(e)
            stop_event.set()
            browser.close()
        

    def run_haully(playwright):
        while True:
            try:
                run_browser()
            except Exception as e:
                run_browser()
                time.sleep(180)

    with sync_playwright() as playwright:
        run_haully(playwright)


if __name__ == "__main__":
    main()
