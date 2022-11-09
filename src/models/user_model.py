import random
import string
from typing import overload


class User(object):
    def __init__(self, name=None, surname=None, login=None) -> None:
        self.name = name
        self.surname = surname
        self.login = login
        print("User Created")

    def __str__(self):
        return f"User name: {self.name}\nUser surname: {self.surname}\nLogin: {self.login} "

    def __del__(self):
        print(f"User {self.name} deleted\n")

    def generate_password(self):
        self.password = "".join(random.choice(string.ascii_letters) for i in range(10))
        print(f"Password generated: {self.password}")

    def set_name(self, value):
        self.name = value
