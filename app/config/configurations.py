import json
import os
from typing import List, Literal
from app.interfaces.config_settings_interface import Config_Settings_Base
from app.utils.helpers import SingleInstanceMetaClass, get_env_variable


class DBConfig(Config_Settings_Base, metaclass=SingleInstanceMetaClass):
    app_root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    current_dir = os.path.dirname(os.path.abspath(__file__))

    Logs: dict = None
    MONGO_HOST: str = None
    MONGO_PORT: int = None
    MONGO_URI: str = None
    MONGO_ENV: Literal["DEV", "PYTEST", "STAGE", "PRODUCTION"] = None
    MONGO_USERNAME: str = None
    MONGO_PASSWORD: str = None

    def load(self, config_path='config.json'):
        config_json_path = os.path.join(DBConfig.current_dir, config_path)
        config_json = json.loads(open(config_json_path, 'r').read())

        DBConfig.Logs = config_json["db_details"]["Logs"]
        DBConfig.MONGO_HOST = get_env_variable("MONGO_HOST", config_json["mongo_details"], str)
        DBConfig.MONGO_PORT = get_env_variable("MONGO_PORT", config_json["mongo_details"], int)
        DBConfig.MONGO_URI = get_env_variable("MONGO_URI", config_json["mongo_details"], str)
        DBConfig.MONGO_ENV = get_env_variable("MONGO_ENV", config_json["mongo_details"], str)
        DBConfig.MONGO_USERNAME = get_env_variable("MONGO_USERNAME", config_json["mongo_details"], str)
        DBConfig.MONGO_PASSWORD = get_env_variable("MONGO_PASSWORD", config_json["mongo_details"], str)


class AppConfig(Config_Settings_Base, metaclass=SingleInstanceMetaClass):
    app_root_dir: str = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__)))
    current_dir: str = os.path.dirname(os.path.abspath(__file__))

    TITLE: str = None
    VERSION: str = None
    DESCRIPTION: str = None
    HOST: str = None
    PORT: int = None
    RELOAD: bool = None
    DEBUG: bool = None
    PUBLIC_URL: str = None
    SERVER_HOST: str = None
    
    def load(self, config_path='config.json'):
        config_json_path = os.path.join(AppConfig.current_dir, config_path)
        config_json = json.loads(open(config_json_path, 'r').read())

        json_dict = config_json["app_details"]

        AppConfig.TITLE = get_env_variable("TITLE", json_dict, str)
        AppConfig.VERSION = get_env_variable("VERSION", json_dict, str)
        AppConfig.DESCRIPTION = get_env_variable("DESCRIPTION", json_dict, str)
        AppConfig.HOST = get_env_variable("HOST", json_dict, str)
        AppConfig.PORT = get_env_variable("PORT", json_dict, int)
        AppConfig.RELOAD = get_env_variable("RELOAD", json_dict, bool)
        AppConfig.DEBUG = get_env_variable("DEBUG", json_dict, bool)
        # use reverse of urllib.parse.urlsplit, i.e. urlunsplit
        # SplitResult(scheme='http', netloc='www.example.com', path='/index', query='', fragment='')
        # it needs a 5 tuple of the above values
        # urlunsplit(('http', 'localhost:5000', '', "",  ""))
        AppConfig.PUBLIC_URL = get_env_variable("PUBLIC_URL", json_dict, str)
        AppConfig.SERVER_HOST = ":".join([str(AppConfig.HOST), str(AppConfig.PORT)])


class RabbitMQConfig(Config_Settings_Base, metaclass=SingleInstanceMetaClass):
    app_root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    current_dir = os.path.dirname(os.path.abspath(__file__))

    rabbitmq_username: str = "guest"
    rabbitmq_password: str = "guest"
    rabbitmq_host: str = "localhost"
    rabbitmq_port: int = 15672
    rabbitmq_virtual_host: str = "/"
    rabbitmq_exchange: str = None
    rabbitmq_exchange_type: str = None
    rabbitmq_consumer_queue: str = None

    def load(self, config_path='config.json'):
        config_json_path = os.path.join(RabbitMQConfig.current_dir, config_path)
        config_json = json.loads(open(config_json_path, 'r').read())

        json_dict = config_json["rabbitmq_details"]

        RabbitMQConfig.rabbitmq_username = get_env_variable("rabbitmq_username", json_dict, str)
        RabbitMQConfig.rabbitmq_password = get_env_variable("rabbitmq_password", json_dict, str)
        RabbitMQConfig.rabbitmq_host = get_env_variable("rabbitmq_host", json_dict, str)
        RabbitMQConfig.rabbitmq_port = get_env_variable("rabbitmq_port", json_dict, int)
        RabbitMQConfig.rabbitmq_virtual_host = get_env_variable("rabbitmq_virtual_host", json_dict, str)
        RabbitMQConfig.rabbitmq_exchange = get_env_variable("rabbitmq_exchange", json_dict, str)
        RabbitMQConfig.rabbitmq_exchange_type = get_env_variable("rabbitmq_exchange_type", json_dict, str)
        RabbitMQConfig.rabbitmq_consumer_queue = get_env_variable("rabbitmq_consumer_queue", json_dict, str)
        

config_path = 'config.json'
DBConfig().load(config_path)
AppConfig().load(config_path)
RabbitMQConfig().load(config_path)