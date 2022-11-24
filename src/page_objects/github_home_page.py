from selenium.webdriver.common.by import By
from src.base.base_element import BaseElement


class GithubHomePage:
    def __init__(self, url, driver) -> None:
        self.url = url
        self.driver = driver

    def go_to_home(self):
        self.driver.get(self.url)

    def go_to_login(self):
        self.driver.get(self.url)
        self.sign_in_button().click()

    def sign_in_button(self):
        return BaseElement(
            driver=self.driver, by=By.CSS_SELECTOR, value="[href='/login']"
        )

    def login_input(self):
        return BaseElement(driver=self.driver, by=By.ID, value="login_field")

    def password_input(self):
        return BaseElement(driver=self.driver, by=By.ID, value="password")

    def login_button(self):
        return BaseElement(
            driver=self.driver, by=By.CSS_SELECTOR, value="[value='Sign in']"
        )

    def login_error_message(self):
        return BaseElement(
            driver=self.driver,
            by=By.CSS_SELECTOR,
            value=".js-flash-alert[role='alert']",
        )

    def avatar_menu_dropdown(self):
        return BaseElement(
            driver=self.driver,
            by=By.CSS_SELECTOR,
            value=".js-feature-preview-indicator-container",
        )

    def login(self, username, password):
        self.login_input().sendText(username)
        self.password_input().sendText(password)
        self.login_button().click()

    def find_element_in_dropdown(self, element):
        return BaseElement(
            driver=self.driver,
            by=By.XPATH,
            value=f"//form/button[contains(text(),'{element}')]",
        )
