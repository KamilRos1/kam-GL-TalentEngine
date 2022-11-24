import requests

from src.data.trello_api_data import Trello_data


class TrelloAPI:
    def __init__(self, *, api_key, token) -> None:
        self.base_url = Trello_data.trello_base_url
        self.api_key = api_key
        self.token = token

    def get_boards(self):
        params = {"key": self.api_key, "token": self.token}
        url = self.base_url + Trello_data.boards_endpoint
        response = requests.get(url=url, params=params)
        return response

    def get_board_by_id(self, id):
        url = self.base_url + Trello_data.board_endpoint + f"/{id}"
        params = {"key": self.api_key, "token": self.token}
        response = requests.get(url=url, params=params)
        return response

    def post_new_board(self, name):
        url = self.base_url + Trello_data.board_endpoint
        params = {"name": name, "key": self.api_key, "token": self.token}
        response = requests.post(url=url, params=params).json()
        return response["id"], response["name"]

    def delete_board(self, id):
        url = self.base_url + Trello_data.board_endpoint + f"/{id}"
        params = {"key": self.api_key, "token": self.token}
        response = requests.delete(url=url, params=params)
        if response.status_code != 200:
            print(f"Status code: {response.status_code}")
            raise Exception("Board cannot be deleted")

    def create_list(self, board_id, name):
        url = self.base_url + Trello_data.list_endpoint
        params = {
            "name": name,
            "idBoard": board_id,
            "key": self.api_key,
            "token": self.token,
        }
        response = requests.post(url=url, params=params)
        return response
