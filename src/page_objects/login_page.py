from selenium.webdriver.common.by import By

from src.base.base_element import BaseElement
from src.base.base_page import BasePage


class LoginPage(BasePage):
    """
    Class contains:
        Components from Github login page
        Methods:
            - Login (log in to github page)
    """

    # Locators
    log_in_input_locator = (By.ID, "login_field")
    sign_in_button_locator = (By.CSS_SELECTOR, "[value='Sign in']")
    password_input_locator = (By.ID, "password")
    login_error_message_locator = (By.CSS_SELECTOR, ".js-flash-alert[role='alert']")
    forgot_password_button_locator = (By.CSS_SELECTOR, "[href='/password_reset']")

    # Components
    @property
    def sign_in_button(self):
        return BaseElement(driver=self.driver, locator=self.sign_in_button_locator)

    @property
    def login_input(self):
        return BaseElement(driver=self.driver, locator=self.log_in_input_locator)

    @property
    def password_input(self):
        return BaseElement(driver=self.driver, locator=self.password_input_locator)

    @property
    def login_error_message(self):
        return BaseElement(driver=self.driver, locator=self.login_error_message_locator)

    @property
    def forgot_password_button(self):
        return BaseElement(
            driver=self.driver, locator=self.forgot_password_button_locator
        )

    # Methods
    def login(self, username, password):
        """
        Method to login on github page
        Args:
            username: username or email address
            password: user password
        """
        self.login_input.sendText(username)
        self.password_input.sendText(password)
        self.sign_in_button.click()
