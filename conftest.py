from datetime import datetime

from pytest import fixture
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from src.applications.github_ui import GithubUi
from src.applications.trello_API import TrelloAPI
from src.config.config import config
from src.models.user_model import User


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
        choices=["chrome", "firefox"],
        default="chrome",
        help="choose firefox or chrome",
    )


@fixture(scope="function")
def browser_webdriver(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        service_obj = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = webdriver.Chrome(service=service_obj, options=options)
    elif browser == "firefox":
        service_obj = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service_obj)
    request.cls.driver = driver
    yield driver
    driver.quit()


@fixture
def github_login(chrome_webdriver):
    github_ui = GithubUi(url=config.conf_dict["URL_GITHUB_UI"], driver=chrome_webdriver)
    github_ui.go_to_login()
    github_ui.login(
        config.conf_dict["GITHUB_LOGIN"],
        config.conf_dict["GITHUB_PASSWORD"],
    )
    yield github_ui
