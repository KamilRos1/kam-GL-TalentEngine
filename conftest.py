from datetime import datetime
from pytest import fixture
from src.page_objects.github_home_page import GithubHomePage
from src.applications.trello_API import TrelloAPI
from src.config.config import config
from src.models.user_model import User
from src.providers.driver_provider.driver_provider import DriverProvider


@fixture(scope="class")
def configuration(request):
    print("Configuration added")

    print(
        f"Base Url: {config.conf_dict['BASE_URL']}\nSQL: {config.conf_dict['SQL_CONNECTION_STRING']}\n"
    )
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
        help="Browser not supported, use chrome, firefox or edge",
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
    github_home_page = GithubHomePage(
        url=config.conf_dict["URL_GITHUB_UI"], driver=browser_webdriver
    )
    github_home_page.go_to_login()
    github_home_page.login(
        config.conf_dict["GITHUB_LOGIN"],
        config.conf_dict["GITHUB_PASSWORD"],
    )
    yield github_home_page
