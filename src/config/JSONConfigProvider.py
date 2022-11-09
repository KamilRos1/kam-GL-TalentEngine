from BaseProvider import BaseProviderClass
from typing import Any
import json


class JSONConfigProvider(BaseProviderClass):
    """
    Class to provide data from JSON file
    """

    @staticmethod
    def _read_config(config_path):
        """
        Opens JSON file and convert it to dict
        Args:
            config_path: Path to JSON file
        Returns
            Dict from file
        """
        with open(config_path) as json_file:
            return json.load(json_file)

    @staticmethod
    def get(item_name) -> Any:
        """
        Gets value from readed dictionary
        Args:
            item_name: Key from dictionary
        Returns:
            Key's value
        """
        value = JSONConfigProvider._read_config("envs_configs/dev.json")
        return value.get(item_name)
