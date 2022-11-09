from typing import Any


class BaseProviderClass:
    """
    Class with methods to inherit for providers
    """

    @staticmethod
    def get(item_name: str) -> Any:
        """
        Raises error when get method not implemented
        """
        raise NotImplementedError("get method not implemented")
