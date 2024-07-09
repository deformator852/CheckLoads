from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import config


class Haully:
    def __init__(self, driver: Firefox) -> None:
        self.driver: Firefox = driver
        self.wait = WebDriverWait(self.driver, 10)

    def start(self, url):
        self.driver.get(url)
        self.__authorization()

    def __check_truck():
        pass
        # if when you restarte the page that check trucks and you unlogined,then use again __authorization

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
        login.click()
