import pika
from pika.exchange_type import ExchangeType

def on_message_recieved(ch, method, properties, body):
    print(f"recieved message: {body}")

connection_parameters = pika.ConnectionParameters()
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_declare(exchange="headersexchange", exchange_type=ExchangeType.headers)

channel.queue_declare(queue="letterbox", durable=True)

bind_arg = {
    "x-match" : "any",
    "name" : "Daniel",
    "age" : 53,
}

channel.queue_bind(queue="letterbox", exchange="headersexchange", arguments=bind_arg)

channel.basic_consume(queue="letterbox", auto_ack=True, on_message_callback=on_message_recieved)

print("starting consuming")

channel.start_consuming()