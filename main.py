from pydantic import BaseModel
from threading import Thread
from typing import List, Set
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from app.config.configurations import AppConfig, DBConfig
from app.events.rabbitmq_event_handler import RabbitMQEventHandler
from app.db.handlers import logs_handler


app_config_text = AppConfig.print()
db_config_text = DBConfig.print()

TITLE = AppConfig.TITLE
VERSION = AppConfig.VERSION
DESCRIPTION = AppConfig.DESCRIPTION

HOST = AppConfig.HOST
PORT = AppConfig.PORT
RELOAD = AppConfig.RELOAD
DEBUG = AppConfig.DEBUG


app = FastAPI(title=TITLE, version=VERSION,
              description=DESCRIPTION)

app.add_middleware(CORSMiddleware, allow_origins=["*"],
                   allow_credentials=True, allow_methods=["*"], allow_headers=["*"])


if __name__ == "__main__":
    rabbitmq_consumer_thread = Thread(
        target=RabbitMQEventHandler.start_consumer, args=())
    rabbitmq_consumer_thread.start()
    uvicorn.run("main:app", host=HOST, port=PORT, reload=RELOAD, debug=DEBUG)
