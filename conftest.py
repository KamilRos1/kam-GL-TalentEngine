from pytest import fixture
from src.config.config import config
from src.models.user_model import User
from datetime import datetime


@fixture(scope="class")
def configuration():
    print("Configuration added")
    print(
        f"Base Url: {config.conf_dict['BASE_URL']}\nSQL: {config.conf_dict['SQL_CONNECTION_STRING']}\n"
    )


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
