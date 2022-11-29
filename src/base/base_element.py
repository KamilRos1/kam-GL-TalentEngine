from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseElement(object):
    """
    Class used to create page components.
    Provides the methods you need for tests with added explicit waits.
    To create BaseElement you need driver and locator of component (by, value)
    """

    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.web_element = None
        self.find_element()

    def find_element(self):
        """
        Find element in DOM, method waits for web element to be visible and adds it to class attributes
        """
        self.web_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locator),
            message=f"Element not found",
        )

    def click(self):
        """
        Method waits for element to be clickable and clicks it
        """
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locator), message="Element is not clickable"
        )
        element.click()

    def text(self):
        """
        Method returns text of component (like button text)
        """
        return self.web_element.text

    def sendText(self, text):
        """
        Method sends text to component (for inputs)
        Args:
            text: Text to forward
        """
        self.web_element.clear()
        self.web_element.send_keys(text)

    def checkVisibility(self):
        """
        Method to check if element is visible
        Returns:
            True if element is visible
            False if not
        """
        return self.web_element.is_displayed()

    def exists(self):
        """
        Method to check if element exists in DOM
        Returns:
            True if element exists
            False if not
        """
        if self.web_element:
            return True
        else:
            return False

    def isEnabled(self):
        """
        Method checks if element is enabled
        Returns:
            True if enabled
            False if disabled
        """
        return self.web_element.is_enabled()
