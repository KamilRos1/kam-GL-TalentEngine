from src.providers.driver_provider.base_provider import BaseProvider
from src.providers.driver_provider.library.chrome_browser import ChromeBrowser
from src.providers.driver_provider.library.edge_browser import EdgeBrowser
from src.providers.driver_provider.library.firefox_browser import \
    FirefoxBrowser


class DriverProvider(BaseProvider):
    MAPPER = {
        "chrome": ChromeBrowser,
        "firefox": FirefoxBrowser,
        "edge": EdgeBrowser,
    }

    @classmethod
    def get_driver(cls, browser):
        return cls.MAPPER.get(browser).get_driver()
