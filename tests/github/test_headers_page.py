from pytest import mark

from src.data.github_data import Github_data
from src.page_objects.header_page import HeadersPage


@mark.headersPage
@mark.usefixtures("configuration", "browser_webdriver")
class TestsHeadersdPage:
    def test_github_icon(self, github_login):
        """
        Test checks if github icon directs user to landing page
        """
        headers_page = HeadersPage(url=Github_data.home_page_url, driver=self.driver)
        # go to pull requests page
        headers_page.pull_requests_nav.click()
        headers_page.wait_for_url_change(Github_data.home_page_url)
        # click github icon
        headers_page.gh_icon.click()
        headers_page.wait_for_url_change(Github_data.pull_requests_url)
        assert headers_page.get_title() == Github_data.landing_page_title

    def test_logout(self, github_login):
        """
        Test checks if user is able to log out
        """
        headers_page = HeadersPage(url=Github_data.home_page_url, driver=self.driver)
        headers_page.logout()
        assert headers_page.get_title() == Github_data.home_page_title
