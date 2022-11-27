from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from src.providers.driver_provider.base_provider import BaseProvider


class ChromeBrowser(BaseProvider):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    @classmethod
    def get_driver(cls):
        service_obj = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service_obj, options=cls.options)
        return driver
