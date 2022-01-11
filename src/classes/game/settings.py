import json
from ...utils.exception_handler import exception_handler

"""
Settings
========

A class for managing in-game settings such as screen size, controllers, and other
game functionalities and bahaviours.
"""
class Settings:
    @exception_handler
    def __init__(self, file = "./settings.json"):
        with open(file, "r") as f:
            self.file = file
            self.settings = json.load(f)

    @exception_handler
    def save(self, file = None):
        with open(file if file else self.file, "w+") as f:
            json.dump(self.settings, f)

    @exception_handler
    def update(self, name, *args):
        func = {
            "file": self.update_file,
            "value": self.update_value
        }.get(name)
        return func(*args)

    @exception_handler
    def update_file(self, file):
        self.file = file

    @exception_handler
    def update_value(self, key, value):
        self.settings[key] = value