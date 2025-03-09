import pika
from pika.exchange_type import ExchangeType
from pika.spec import BasicProperties

connection_parameters = pika.ConnectionParameters()
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_declare(exchange="headersexchange", exchange_type=ExchangeType.headers)

message = "This message will be sent with headers"

channel.basic_publish(
    exchange="headersexchange", 
    routing_key="", 
    body=message,
    
    properties=BasicProperties(
        headers = {
            "name" : "Daniel"
        }
    )
    
)

print(f"sent message: {message}")

connection.close()