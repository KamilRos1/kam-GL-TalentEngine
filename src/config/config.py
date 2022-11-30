import sys
from typing import Any

sys.path.append("home/kamros/Desktop/kam-GL-TalentEngine")
from src.providers.JSONConfigProvider import JSONConfigProvider
from src.providers.OSConfigProvider import OSConfigProvider


class Config:
    """
    Holds all the settings of framework
    """

    def __init__(self, config_providers) -> None:
        """
        Initialize class with config_providers
        Args:
            config_provider - Chosen config provider
        """
        self.config_providers = config_providers
        self.conf_dict = {}
        self._register("API_KEY")
        self._register("TOKEN")
        self._register("GITHUB_LOGIN")
        self._register("GITHUB_PASSWORD")
        self._register("URL_GITHUB_UI")
        self._register("SELENIUM_GRID_URL")

    def get(self, item_name: str) -> Any:
        """
        Return value from conf_dict
        Args:
            item_name - key to search
        Returns:
            Value of item_namew
        """
        return self.conf_dict[item_name]

    def _register(self, item_name: str) -> Any:
        """
        Search for item in providers and register it, if not found raises ValueError
        Args:
            item - Item to register
        """
        for provider in self.config_providers:
            value = provider.get(item_name)
            if value is not None:
                self.conf_dict[item_name] = value
                return
        raise ValueError(f"{item_name} name is missing in config providers")


config = Config([JSONConfigProvider, OSConfigProvider])
