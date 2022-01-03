import json
import pika

from app.config.configurations import RabbitMQConfig
from app.db.handlers import logs_handler

class RabbitMQConsumer:
    def __init__(self, rabbitmq_config: RabbitMQConfig) -> None:
        self.rabbitmq_config = rabbitmq_config

    def start_consuming(self):
        username = self.rabbitmq_config.rabbitmq_username
        password = self.rabbitmq_config.rabbitmq_password
        host = self.rabbitmq_config.rabbitmq_host
        port = self.rabbitmq_config.rabbitmq_port
        virtual_host = self.rabbitmq_config.rabbitmq_virtual_host
        credentials = pika.PlainCredentials(username, password)
        # parameters = pika.ConnectionParameters(host=host, port=port, virtual_host=virtual_host, credentials=credentials)
        parameters = pika.ConnectionParameters(host=host, virtual_host=virtual_host, credentials=credentials)
        connection = pika.BlockingConnection(parameters=parameters)
        channel = connection.channel()

        def callback(ch, method, properties, body):
            # insert the message into db
            message = json.loads(body.decode("UTF-8"))
            logs_handler.insert(message)
            
    
        exchange = self.rabbitmq_config.rabbitmq_exchange
        exchange_type = self.rabbitmq_config.rabbitmq_exchange_type
        queue_name = self.rabbitmq_config.rabbitmq_consumer_queue

        # if exchange_type == "direct":
        #     # add server name to the queue binding? how does it work though?
        #     # should the publisher also specify the name of the server to which the message should be published?
        #     # for now, we'll assume fanout, for the sake of simplicity
        #     channel.queue_declare()

        channel.basic_qos(prefetch_count=1)
        channel.exchange_declare(exchange, exchange_type, durable=True)
        consumer_queue = channel.queue_declare(queue_name, durable=True)
        
        generated_queue_name = consumer_queue.method.queue
        
        channel.queue_bind(queue=generated_queue_name, exchange=exchange)
        channel.basic_consume(queue=generated_queue_name, on_message_callback=callback, auto_ack=True)
        
        channel.basic_qos(prefetch_count=1)
        print("starting consumption")
        channel.start_consuming()


if __name__ == "__main__":
    rabbitmq_consumer = RabbitMQConsumer(RabbitMQConfig)
    rabbitmq_consumer.start_consuming()
