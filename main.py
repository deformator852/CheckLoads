from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.firefox.options import Options
from haully import Haully  # pyright:ignore
import config
import threading


def main():
    options = Options()
    options.add_argument(config.USER_AGENT)
    options.add_argument("--disable-blink-features=AutomationControlled")
    # options.add_argument('headless')
    stop_event = threading.Event()
    options.add_argument("window-size=1920,1080")
    driver = webdriver.Firefox(options)
    haully = Haully(driver)
    haully_thread = threading.Thread(target=haully.start("https://www.haully.com/"))
    try:
        haully_thread.start()
    except Exception as e:
        print(e)
    finally:
        stop_event.set()
        driver.quit()


if __name__ == "__main__":
    main()
