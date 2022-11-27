from pytest import mark

from src.data.github_data import Github_data
from src.page_objects.landing_page import LandingPage


@mark.landingPage
@mark.usefixtures("configuration", "browser_webdriver")
class TestsLandingPage:
    def test_logout(self, github_login):
        """
        Test checks if user is able to log out
        """
        landing_page = LandingPage(url=Github_data.login_page_url, driver=self.driver)
        landing_page.logout()
        assert landing_page.get_title() == Github_data.home_page_title
