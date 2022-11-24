import pytest

from src.data.trello_api_data import Trello_data


@pytest.mark.trelloAPI
@pytest.mark.usefixtures("configuration", "create_trello_instance")
class TestsTrelloAPI:
    def test_check_status_code(self):
        response = self.trello.get_boards()
        assert (
            response.status_code == 200
        ), f"Status code is {response.status_code}, should be 200"

    @pytest.mark.parametrize("header, expected", Trello_data.headers)
    def test_check_headers(self, header, expected):
        response = self.trello.get_boards()
        assert response.headers[header] == expected, f"{header} should be {expected}"

    def test_get_board(self):
        response = self.trello.get_board_by_id(Trello_data.learning_api_board_id)
        assert (
            response.json()["name"] == Trello_data.learning_api_board_name
        ), f"Wrong board name, should be {Trello_data.learning_api_board_name}"

    def test_create_new_list(self, create_trello_board):
        board_id = create_trello_board[0]
        response = self.trello.create_list(board_id, Trello_data.list_name).json()
        assert len(response["id"]) != 0, "List was not created, id is empty"
