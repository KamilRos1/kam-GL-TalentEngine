from BaseProvider import BaseProviderClass
from typing import Any
import os


class OSConfigProvider(BaseProviderClass):
    """
    Class to provide data from Operating System
    """

    @staticmethod
    def get(item_name) -> Any:
        """
        Gets value from OS
        Args:
            item_name: Key for searching
        Returns:
            Key's value
        """
        value = os.getenv(item_name)
        return value
