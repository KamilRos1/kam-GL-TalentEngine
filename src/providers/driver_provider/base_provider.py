class BaseProvider:
    """
    Class with method to inherit for providers
    """

    def get_driver(self):
        """
        Method raises error when get_driver method is not implemented in provider class
        """
        raise NotImplementedError("get_driver method is not implemented!")
