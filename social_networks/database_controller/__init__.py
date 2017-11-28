from social_networks.database_controller.database import Database
from social_networks.database_controller.read import ReadFromDatabase
from social_networks.database_controller.write import WriteToDatabase

import os

__all__ = [
    "Database",
    "ReadFromDatabase",
    "WriteToDatabase"]

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

__credential_file__ = os.path.join(__location__, "mongo_connect")
