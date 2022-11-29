from pytest import mark

from src.data.github_data import Github_data
from src.page_objects.home_page import HomePage


@mark.homePage
@mark.usefixtures("configuration", "browser_webdriver")
class TestsHomePage:
    def test_sign_in_redirect(self):
        """
        Test checks if sing in button redirect user to correct page
        """
        home_url = self.config.conf_dict["URL_GITHUB_UI"]
        home_page = HomePage(url=home_url, driver=self.driver)
        home_page.go_to()
        home_page.sign_in_button.click()
        home_page.wait_for_url_change(url=home_url)
        assert home_page.get_title() == Github_data.login_page_title

    def test_sing_up_redirect(self):
        """
        Test checks if sing up button redirect user to correct page
        """
        home_url = self.config.conf_dict["URL_GITHUB_UI"]
        home_page = HomePage(url=home_url, driver=self.driver)
        home_page.go_to()
        home_page.sign_up_button.click()
        home_page.wait_for_url_change(url=home_url)
        assert home_page.get_title() == Github_data.sign_up_page_title
