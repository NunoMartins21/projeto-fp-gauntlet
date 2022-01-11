import sys

def exception_handler(func):
    def inner(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as err:
            print(f"[{sys.modules[__name__]}] Something went wrong! - {err}")
    return inner