from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):
    """
    Class contains methods to inherit for Page object classes
    """

    def __init__(self, url, driver):
        """
        Init method, requires page url and driver
        """
        self.url = url
        self.driver = driver

    def go_to(self):
        """
        Method opens page, uses the url from class attributes
        """
        self.driver.get(self.url)

    def wait_for_url_change(self, url, timeout=10):
        """
        Method waits for ulr change.
        Args:
            url: Url supposed to change
        """
        wait = WebDriverWait(self.driver, timeout)
        wait.until(lambda driver: driver.current_url != url)

    def get_title(self):
        """ "
        Method to check actual title of the page
        Returns:
            Title of the page
        """
        return self.driver.title
