from app.config.configurations import RabbitMQConfig
from app.events.rabbitmq_consumer import RabbitMQConsumer
from app.events.rabbitmq_publisher import RabbitMQPublisher
from app.utils.helpers import SingleInstanceMetaClass


class RabbitMQEventHandler(metaclass=SingleInstanceMetaClass):
    rabbitmq_config: RabbitMQConfig = None
    consumer: RabbitMQConsumer = None
    publisher: RabbitMQPublisher = None
    
    def __init__(self, rabbitmq_config) -> None:
        RabbitMQEventHandler.rabbitmq_config = rabbitmq_config
        RabbitMQEventHandler.consumer = RabbitMQConsumer(rabbitmq_config)
        RabbitMQEventHandler.publisher = RabbitMQPublisher(rabbitmq_config)

    @classmethod
    def start_consumer(cls):
        RabbitMQEventHandler.consumer.start_consuming()

    @classmethod
    def publish_message(cls, message):
        RabbitMQEventHandler.publisher.publish(message)

RabbitMQEventHandler(RabbitMQConfig)
