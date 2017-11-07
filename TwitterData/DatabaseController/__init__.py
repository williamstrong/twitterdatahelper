import os

__all__ = [
    "Database",
    "Read",
    "Write"]

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

__credential_file__ = os.path.join(__location__, "mongo_connect")