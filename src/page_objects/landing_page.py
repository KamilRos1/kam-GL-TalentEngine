from selenium.webdriver.common.by import By

from src.base.base_element import BaseElement
from src.base.base_page import BasePage


class LandingPage(BasePage):
    """
    Class contains:
        Components from Github landing page
        Methods:
            - logout (log out of the github page)
    """

    # Locators
    avatar_locator = (By.CSS_SELECTOR, ".js-feature-preview-indicator-container")

    # Components
    @property
    def avatar_menu_dropdown(self):
        return BaseElement(driver=self.driver, locator=self.avatar_locator)

    def find_element_in_dropdown(self, element):
        """
        Method to choose button from menu dropdown (avatar icon)
        Args:
            element: Button text (settings, help, upgrade, etc.)
        Returns:
            BaseElement representing button from dropdown
        """
        return BaseElement(
            driver=self.driver,
            locator=(By.XPATH, f"//form/button[contains(text(),'{element}')]"),
        )

    # Methods
    def logout(self):
        """
        Log out of the github site
        """
        self.avatar_menu_dropdown.click()
        self.find_element_in_dropdown("Sign out").click()
