import json
import pika

from app.config.configurations import RabbitMQConfig

class RabbitMQPublisher:
    def __init__(self, rabbitmq_config: RabbitMQConfig) -> None:
        self.rabbitmq_config = rabbitmq_config

    def publish(self, message: dict):
        # first convert message to json
        json_message = json.dumps(message)
        # maybe later, I'll use amqpstorm library's Message and Connection classes to create a connection and a RabbitMQ message, respectively
        # rabbitmq_message = json_message
        
        
        username = self.rabbitmq_config.rabbitmq_username
        password = self.rabbitmq_config.rabbitmq_password
        host = self.rabbitmq_config.rabbitmq_host
        port = self.rabbitmq_config.rabbitmq_port
        virtual_host = self.rabbitmq_config.rabbitmq_virtual_host
        credentials = pika.PlainCredentials(username, password)
        # parameters = pika.ConnectionParameters(host=host, port=port, virtual_host=virtual_host, credentials=credentials)
        parameters = pika.ConnectionParameters(host=host, virtual_host=virtual_host, credentials=credentials)
        connection = pika.BlockingConnection(parameters=parameters)
        
        exchange = self.rabbitmq_config.rabbitmq_exchange
        exchange_type = self.rabbitmq_config.rabbitmq_exchange_type
        
        channel = connection.channel()
        channel.exchange_declare(exchange=exchange, exchange_type=exchange_type, durable=True)
        channel.basic_publish(exchange=exchange, routing_key="", body=json_message, properties=pika.BasicProperties(delivery_mode=2))
        connection.close()

        
if __name__ == "__main__":
    rabbitmq_publisher = RabbitMQPublisher(RabbitMQConfig)
    rabbitmq_publisher.publish("Hello there")
