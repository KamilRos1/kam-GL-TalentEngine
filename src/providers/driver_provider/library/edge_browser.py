from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from src.providers.driver_provider.base_provider import BaseProvider


class EdgeBrowser(BaseProvider):
    options = webdriver.EdgeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    @classmethod
    def get_driver(cls):
        service_obj = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service_obj, options=cls.options)

        return driver
