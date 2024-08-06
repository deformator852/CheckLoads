from playwright.sync_api import Page, sync_playwright
from bot import send_load
from utils import export_price
import config
import time
import web_selectors as selectors

class Haully:
    def __init__(self, page: Page) -> None:
        self.page: Page = page
        self.last_load_id = None

    def start(self, url):
        self.page.goto(url)
        time.sleep(1)
        self.__authorization()
        self.__go_to_search()
        while True:
            self.__check_loads()
            time.sleep(60)

    def __check_count_vehicles(self) -> int:
        vehicles = self.page.wait_for_selector(selectors.VEHICLES).inner_text().strip()
        vehicle = vehicles[0]
        if vehicle.isdigit():
            return int(vehicle)
        else:
            raise Exception("Vehicle in __check_count_vehicle not digit!")

    def __check_loads(self):
        self.page.reload()
        load: dict = self.__get_last_load()
        load_price = int(load.get("price"))
        load_id = load.get("id")
        load_price = int(load_price)
        filter_price = export_price()
        if load_price >= filter_price:
            count_vehicle = 5
            try:
                count_vehicle = self.__check_count_vehicles()
            except Exception as e:
                print(e)
            if self.last_load_id != load_id and count_vehicle <= 6:
                print("new load")
                send_load(load_price, load_id)
                self.last_load_id = load_id
            #else:
            #   print("Spend five minutes! No new load!")

    def __get_last_load(self) -> dict:
        self.page.wait_for_selector(
            "div.src-hocs-withBackground__Background-light-gray--OlGgA:nth-child(3) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)"
        )
        load_price = (
            self.page.query_selector(
              selectors.LOAD_PRICE 
            )
            .inner_text()
            .strip()
        ).replace(",", "")
        load_id = (
            self.page.query_selector(
               selectors.LOAD_ID 
            )
            .inner_text()
            .strip()
        )
        return {"price": load_price[1:-3], "id": load_id}

    def __go_to_search(self):
        search_button_selector = selectors.SEARCH_BUTTON
        self.page.wait_for_selector(search_button_selector)
        time.sleep(2)
        self.page.click(search_button_selector)
        time.sleep(3)

    def __authorization(self):
        login_button_selector = selectors.LOGIN_BUTTON
        self.page.wait_for_selector(login_button_selector)
        self.page.click(login_button_selector)

        form_selector = selectors.FORM
        self.page.wait_for_selector(form_selector)
        email_field = self.page.query_selector("#email")
        password_field = self.page.query_selector("#password")
        email_field.fill(config.EMAIL)
        password_field.fill(config.PASSWORD)
        login_button_selector = "button.src-components-Button__PrimaryButton--3aiuT"
        self.page.wait_for_selector(login_button_selector)
        time.sleep(3)
        self.page.click(login_button_selector)


# def main():
#     stop_event = threading.Event()
#
#     def run_haully(playwright):
#         browser = playwright.chromium.launch(headless=True)
#         context = browser.new_context(
#             user_agent=config.USER_AGENT, viewport={"width": 1920, "height": 1080}
#         )
#         page = context.new_page()
#         haully = Haully(page)
#         haully_thread = threading.Thread(
#             target=haully.start, args=("https://www.haully.com/",)
#         )
#         try:
#             haully_thread.start()
#         except Exception as e:
#             print(e)
#         finally:
#             stop_event.set()
#             browser.close()
#
#     with sync_playwright() as playwright:
#         run_haully(playwright)


# if __name__ == "__main__":
#     main()
