import pika
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters()
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_declare(exchange="routing", exchange_type=ExchangeType.direct)

message1 = "this message for analytics"
message2 = "this message for payments"

channel.basic_publish(exchange="routing", routing_key="analytics", body=message1)
channel.basic_publish(exchange="routing", routing_key="payments", body=message2)

print(f"sent message: {message1}")
print(f"sent message: {message2}")

channel.close()