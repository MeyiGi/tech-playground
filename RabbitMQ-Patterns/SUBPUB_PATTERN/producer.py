import pika
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.queue_declare(queue="")

channel.exchange_declare(exchange="pubsub", exchange_type=ExchangeType.fanout)

message = "Hello from product.py!"

channel.basic_publish(exchange="pubsub", routing_key="", body=message)

print("sent message: ", message)

channel.close()