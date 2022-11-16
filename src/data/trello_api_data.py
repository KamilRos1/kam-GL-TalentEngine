class Trello_data:
    trello_base_url = "https://api.trello.com/1"
    boards_endpoint = "/members/me/boards"
    board_endpoint = "/boards"
    list_endpoint = "/lists"
    learning_api_board_id = "63721b7d3136e00108ef8515"
    learning_api_board_name = "Learning API"
    list_name = "List number one"
    headers = [
        ("Content-Type", "application/json; charset=utf-8"),
        ("Content-Encoding", "gzip"),
    ]
