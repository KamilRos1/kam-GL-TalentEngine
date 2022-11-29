from pytest import mark

from src.page_objects.github_home_page import GithubHomePage
from src.data.github_data import Github_data


@mark.githubLogin
@mark.usefixtures("configuration", "browser_webdriver")
class TestsGithubLogin:
    def test_homepage(self):
        home_page = GithubHomePage(
            url=self.config.conf_dict["URL_GITHUB_UI"], driver=self.driver
        )
        home_page.go_to_home()
        assert self.driver.title == Github_data.home_page_title

    def test_login_positive(self):
        home_page = GithubHomePage(
            url=self.config.conf_dict["URL_GITHUB_UI"], driver=self.driver
        )
        home_page.go_to_login()
        home_page.login(
            self.config.conf_dict["GITHUB_LOGIN"],
            self.config.conf_dict["GITHUB_PASSWORD"],
        )
        assert self.driver.title == Github_data.logged_title

    def test_login_negative(self):
        home_page = GithubHomePage(
            url=self.config.conf_dict["URL_GITHUB_UI"], driver=self.driver
        )
        home_page.go_to_login()
        home_page.login(Github_data.wrong_login, Github_data.wrong_password)
        assert home_page.login_error_message.checkVisibility()

    def test_logout(self, github_login):
        github_login.avatar_menu_dropdown.click()
        github_login.find_element_in_dropdown("Sign out").click()
        assert self.driver.title == Github_data.home_page_title
