from selenium.webdriver.common.by import By

from src.base.base_element import BaseElement
from src.base.base_page import BasePage


class ForgotPasswordPage(BasePage):
    """
    Class contains:
        Components from Github forgot password page
    """

    # Locators
    email_field_locator = (By.ID, "email_field")
    send_reset_email_locator = (
        By.CSS_SELECTOR,
        "input[value='Send password reset email']",
    )

    # Components
    @property
    def email_input(self):
        return BaseElement(driver=self.driver, locator=self.email_field_locator)

    @property
    def send_reset_email_button(self):
        return BaseElement(driver=self.driver, locator=self.send_reset_email_locator)
