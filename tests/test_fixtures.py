import pytest

from src.config.config import config


@pytest.mark.skip(reason="temporary disabled")
@pytest.mark.fixtureTests
@pytest.mark.usefixtures("execution_time", "configuration")
class TestsFixtures:
    def test_check_base_url(self):
        assert config.conf_dict["BASE_URL"] == "google.com", "Wrong Base Url"

    @pytest.mark.parametrize(
        "name, surname, login",
        [["John", "Smith", "J.Smith"], ["Eve", "Json", "E.Json"]],
    )
    def test_check_user(self, user, name):
        print(user)
        expected = name
        assert user.name == expected, f"User name {user.name} should be {expected} "

    @pytest.mark.parametrize("name, surname, login", [["John", "Smith", "J.Smith"]])
    def test_password_generator(self, user):
        user.generate_password()
        assert user.password is not None, "Password was not generated"
