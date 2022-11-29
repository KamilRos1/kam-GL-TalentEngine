from selenium.webdriver.common.by import By

from src.base.base_element import BaseElement
from src.base.base_page import BasePage


class HeadersPage(BasePage):
    """
    Class contains:
        Components from Github home page

    """

    # Locators
    gh_icon_locator = (By.XPATH, "(//header/div/a[@data-hotkey='g d'])[1]")
    pull_requests_nav_locator = (By.CSS_SELECTOR, "a[aria-label*='requests']")
    issues_nav_locator = (By.CSS_SELECTOR, "a[aria-label*='Issues']")
    codespaces_nav_locator = (By.CSS_SELECTOR, "a[data-ga-click*='workspaces']")
    marketplace_nav_locator = (By.CSS_SELECTOR, "a[data-ga-click*='marketplace']")
    explore_nav_locator = (By.CSS_SELECTOR, "a[data-ga-click*='explore']")
    notification_nav_locator = (By.CSS_SELECTOR, "a[data-target*='notification']")
    avatar_nav_locator = (By.CSS_SELECTOR, ".js-feature-preview-indicator-container")

    # Components
    @property
    def gh_icon(self):
        return BaseElement(driver=self.driver, locator=self.gh_icon_locator)

    @property
    def pull_requests_nav(self):
        return BaseElement(driver=self.driver, locator=self.pull_requests_nav_locator)

    @property
    def issues_nav(self):
        return BaseElement(driver=self.driver, locator=self.issues_nav_locator)

    @property
    def codespaces_nav(self):
        return BaseElement(driver=self.driver, locator=self.codespaces_nav_locator)

    @property
    def marketplace_nav(self):
        return BaseElement(driver=self.driver, locator=self.marketplace_nav_locator)

    @property
    def explore_nav(self):
        return BaseElement(driver=self.driver, locator=self.explore_nav_locator)

    @property
    def notification_nav(self):
        return BaseElement(driver=self.driver, locator=self.notification_nav_locator)

    @property
    def avatar_nav(self):
        return BaseElement(driver=self.driver, locator=self.avatar_nav_locator)

    # Methods
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

    def logout(self):
        """
        Log out of the github site
        """
        self.avatar_nav.click()
        self.find_element_in_dropdown("Sign out").click()
