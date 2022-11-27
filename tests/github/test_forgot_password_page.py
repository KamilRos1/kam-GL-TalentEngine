from pytest import mark

from src.data.github_data import Github_data
from src.page_objects.forgot_password_page import ForgotPasswordPage


@mark.forgotPasswordPage
@mark.usefixtures("configuration", "browser_webdriver")
class TestsForgotPasswordPage:
    def test_send_button(self):
        """
        Test checks if button to send reset email is disabled when empty email input and captcha not resolved
        """
        fp_page = ForgotPasswordPage(
            url=Github_data.forgot_password_url, driver=self.driver
        )
        fp_page.go_to()
        assert fp_page.send_reset_email_button.isEnabled() is False
