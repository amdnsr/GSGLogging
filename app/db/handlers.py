from app.db.mongo_handler import MongoHandlerBase
from app.db.log_schema import Logs, logs_connection_info


class LogsHandler(MongoHandlerBase):
    def __init__(self, mongo_connection_info) -> None:
        super().__init__(mongo_connection_info)

    def insert(self, log):
        self.make_connection()

        model_dict = {}
        model_dict["log"] = log
        log_model = Logs(**model_dict)
        db_obj = log_model.save()
        self.close_connection()
        return db_obj
    
    def get_logs(self, count):
        self.make_connection()
        logs = Logs.objects().limit(count)
        print(logs)
        self.close_connection()
        return logs


logs_handler = LogsHandler(logs_connection_info)
