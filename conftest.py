from datetime import datetime
from pytest import fixture
from src.config.config import config
from src.models.user_model import User
from src.applications.trello_API import TrelloAPI


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
def create_trello_board(request, create_trello_instance):
    trello = create_trello_instance
    board_id, name = trello.post_new_board("temBoard")
    yield board_id, name
    trello.delete_board(board_id)
