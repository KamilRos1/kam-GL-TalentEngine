from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseElement(object):
    def __init__(self, driver, value, by):
        self.driver = driver
        self.value = value
        self.by = by
        self.locator = (self.by, self.value)
        self.web_element = None
        self.find_element()

    def find_element(self):
        self.web_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locator),
            message=f"Element {self.value} not found",
        )

    def click(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locator), message="Element is not clickable"
        )
        element.click()

    def text(self):
        return self.web_element.text

    def sendText(self, text):
        self.web_element.clear()
        self.web_element.send_keys(text)

    def checkVisibility(self):
        return self.web_element.is_displayed()

    def exists(self):
        if self.web_element:
            return True
        else:
            return False
