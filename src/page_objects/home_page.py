from selenium.webdriver.common.by import By

from src.base.base_element import BaseElement
from src.base.base_page import BasePage


class HomePage(BasePage):
    """
    Class contains:
        Components from Github home page

    """

    # Locators
    sign_in_button_locator = (By.CSS_SELECTOR, "[href='/login']")
    sign_up_button_locator = (By.XPATH, "//a[normalize-space()='Sign up']")

    # Components
    @property
    def sign_in_button(self):
        return BaseElement(driver=self.driver, locator=self.sign_in_button_locator)

    @property
    def sign_up_button(self):
        return BaseElement(driver=self.driver, locator=self.sign_up_button_locator)
