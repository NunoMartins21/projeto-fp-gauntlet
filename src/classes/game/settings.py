from _typeshed import Self


import json

"""
Settings
========

A class for managing in-game settings such as screen size, controllers, and other
game functionalities and bahaviours.
"""
class Settings:
    def exception_handler(self, func):
        def inner(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except Exception as err:
                print(f"[Settings] Something went wrong! - {err}")
        return inner

    @exception_handler
    def __init__(self, file = "settings.json") -> Self:
        with open(file, "r") as f:
            self.file = file
            self.settings = json.load(f)
        return self

    @exception_handler
    def save(self, file = None) -> Self:
        with open(file if file else self.file, "w+") as f:
            json.dump(self.settings, f)
        return self

    @exception_handler
    def update(self, name, *args) -> Self:
        func = {
            "file": self.update_file,
            "value": self.update_value
        }.get(name)
        return func(*args)

    @exception_handler
    def update_file(self, file) -> Self:
        self.file = file
        return self

    @exception_handler
    def update_value(self, key, value) -> Self:
        self.settings[key] = value
        return self