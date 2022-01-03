from mongoengine import Document
from mongoengine.fields import DictField, StringField
from app.config.configurations import DBConfig

db_config = DBConfig()


class Logs(Document):
    log = StringField()

    meta = {
        'db_alias': db_config.Logs["alias"],
        'collection': db_config.Logs["collection_name"]
    }


logs_connection_info = {
    "alias": "Logs",
    "host_name": db_config.MONGO_HOST,
    "host_port": db_config.MONGO_PORT,
    "db_name": db_config.Logs["db_name"],
    "collection_name": "Logs",
    "mongo_env": db_config.MONGO_ENV,
    "username": db_config.MONGO_USERNAME,
    "password": db_config.MONGO_PASSWORD
}
