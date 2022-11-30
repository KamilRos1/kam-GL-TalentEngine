from src.config.config import config
from src.providers.driver_provider.base_provider import BaseProvider
from selenium import webdriver
from src.config.config import config


class RemoteffBrowser(BaseProvider):
    OPTIONS = None

    @classmethod
    def get_driver(cls):
        driver = webdriver.Remote(
            command_executor=config.conf_dict["SELENIUM_GRID_URL"],
            desired_capabilities={"browserName": "firefox"},
        )

        return driver
