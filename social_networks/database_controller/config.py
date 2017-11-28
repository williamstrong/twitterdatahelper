import configparser
from social_networks.database_controller import __credential_file__


config_file = configparser.ConfigParser()
config_file.read(__credential_file__)



