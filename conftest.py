from datetime import datetime

from pytest import fixture

from src.applications.trello_API import TrelloAPI
from src.config.config import config
from src.data.github_data import Github_data
from src.models.user_model import User
from src.page_objects.login_page import LoginPage
from src.providers.driver_provider.driver_provider import DriverProvider


@fixture(scope="class")
def configuration(request):
    print("Configuration added")
    request.cls.config = config
    yield config


@fixture(scope="session")
def execution_time():
    actual_time = datetime.now()
    print(f"\n\nTest start time: {actual_time.strftime('%H:%M:%S')}\n")
    yield
    actual_time = datetime.now()
    print(f"Test end time: {actual_time.strftime('%H:%M:%S')}")


@fixture(scope="function")
def user(name, surname, login):
    user = User(name, surname, login)
    yield user
    del user


@fixture(scope="class")
def create_trello_instance(request):
    trello = TrelloAPI(
        api_key=config.conf_dict["API_KEY"],
        token=config.conf_dict["TOKEN"],
    )
    request.cls.trello = trello
    yield trello


@fixture
def create_trello_board(create_trello_instance):
    trello = create_trello_instance
    board_id, name = trello.post_new_board("temBoard")
    yield board_id, name
    trello.delete_board(board_id)


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        choices=["chrome", "firefox", "edge"],
        default="chrome",
        help="Use Chrome, Firefox or Edge browser",
    )


@fixture(scope="function")
def browser_webdriver(request):
    browser = request.config.getoption("--browser")
    driver = DriverProvider.get_driver(browser)
    request.cls.driver = driver
    driver.maximize_window()
    yield driver
    driver.quit()


@fixture
def github_login(browser_webdriver):
    login_page = LoginPage(url=Github_data.login_page_url, driver=browser_webdriver)
    login_page.go_to()
    login_page.login(
        config.conf_dict["GITHUB_LOGIN"],
        config.conf_dict["GITHUB_PASSWORD"],
    )
    yield
