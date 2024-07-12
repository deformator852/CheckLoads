from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bot import send_load
from utils import export_price
import config
import time


class Haully:
    def __init__(self, driver: Firefox) -> None:
        self.driver: Firefox = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.last_load_id = None

    def start(self, url):
        self.driver.get(url)
        self.__authorization()
        self.__go_to_search()
        while True:
            self.__check_loads()
            time.sleep(300)

    def __check_loads(self):
        self.driver.refresh()
        last_load = self.__get_last_load()
        load_price = last_load.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/a/div[1]/div[3]/div[1]/div[1]/div[1]",
        ).text[1:-3]
        load_price = load_price.replace(",", "")
        load_price = int(load_price)
        filter_price = export_price()
        if load_price >= filter_price:
            load_id = last_load.find_element(
                By.XPATH,
                "/html/body/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/a/div[1]/div[1]/div[1]",
            ).text
            if self.last_load_id != load_id:
                send_load(load_price, load_id)
                self.last_load_id = load_id
            else:
                print("Spend five minutes!No new load!")

    def __get_last_load(self):
        load = self.wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/a",
                )
            )
        )
        return load

    def __go_to_search(self):
        search = self.wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div[1]/form/div[2]/div[2]/button",
                )
            )
        )
        time.sleep(2)
        search.click()
        time.sleep(3)

    def __authorization(self):
        login_button = self.wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[1]/div/div/div/div[1]/div/button",
                )
            )
        )
        login_button.click()
        form = self.wait.until(EC.visibility_of_element_located((By.ID, "loginForm")))
        email_field = form.find_element(By.ID, "email")
        password_filed = form.find_element(By.ID, "password")
        email_field.send_keys(config.EMAIL)  # pyright:ignore
        password_filed.send_keys(config.PASSWORD)  # pyright:ignore
        login = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div[3]/div/div/div[2]/div/form/button")
            )
        )
        time.sleep(3)
        login.click()
