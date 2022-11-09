from BaseProvider import BaseProviderClass
from typing import Any


class AWSConfigProvider(BaseProviderClass):
    """
    Provider for AWS system (if we had any)
    """

    @staticmethod
    def get(item_name) -> Any:
        """
        Gets value from AWS
        Args:
            item_name: Key for searching
        Returns:
            Key's value
        """
        value = "AWS_SECRETS_VALUE"
        return value
