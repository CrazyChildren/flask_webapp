import configparser
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    def set_config_from_file(self):
        config= configparser.RawConfigParser()
        config.optionxform = lambda option: option

        file_name = f"{dir_path}/config/{self.ENV}.ini"
        config.read(file_name)
        for sections in config.sections():
            for key, value in config[sections].items():
                setattr(self, key, value)
        setattr(self, "SQLALCHEMY_DATABASE_URI", f"mysql://{self.SQL_NAME}:{self.SQL_PASSWD}@{self.SQL_ADDR}") 


class DevConfig(Config):
    DEBUG = "True"
    ENV = "development"

    def __init__(self) -> None:
        super().__init__()
        self.set_config_from_file()

config = {
    "development": DevConfig
}