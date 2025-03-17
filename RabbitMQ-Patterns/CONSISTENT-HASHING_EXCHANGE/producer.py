import pika

connection_parameters = pika.ConnectionParameters()
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_declare("simplehash", "x-consistent-hash")

routing_key = "Hash me!"

message = "this is core message"

channel.basic_publish(
    exchange="simplehash",
    routing_key=routing_key,
    body=message,
    properties=pika.BasicProperties(headers={"name" : "brian"})
)

print(f"sent message: {message}")

connection.close()