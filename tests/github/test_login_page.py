from pytest import mark

from src.data.github_data import Github_data
from src.page_objects.login_page import LoginPage


@mark.loginPage
@mark.usefixtures("configuration", "browser_webdriver")
class TestsLoginPage:
    def test_login_positive(self):
        """
        Test checks if user is able to log in
        """
        login_page = LoginPage(url=Github_data.login_page_url, driver=self.driver)
        login_page.go_to()
        login_page.login(
            self.config.conf_dict["GITHUB_LOGIN"],
            self.config.conf_dict["GITHUB_PASSWORD"],
        )
        login_page.wait_for_url_change(Github_data.login_page_url)
        assert login_page.get_title() == Github_data.landing_page_title

    def test_login_negative(self):
        """
        Test checks if user is not able to log in and gets error while using wrong data
        """
        login_page = LoginPage(url=Github_data.login_page_url, driver=self.driver)
        login_page.go_to()
        login_page.login(Github_data.wrong_login, Github_data.wrong_password)
        assert login_page.login_error_message.checkVisibility()

    def test_forgot_password_redirect(self):
        """
        Test checks if forgot password button redirect user to correct page
        """
        login_page = LoginPage(url=Github_data.login_page_url, driver=self.driver)
        login_page.go_to()
        login_page.forgot_password_button.click()
        login_page.wait_for_url_change(Github_data.login_page_url)
        assert login_page.get_title() == Github_data.forgot_password_page_title
