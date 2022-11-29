from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver


class FirefoxBrowser:
    options = None

    @classmethod
    def get_driver(cls):
        service_obj = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service_obj, options=cls.options)
        return driver
