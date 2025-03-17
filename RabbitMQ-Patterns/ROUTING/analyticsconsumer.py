import pika
from pika.exchange_type import ExchangeType

def message_recieved(ch, method, properties, body):
    print(f"Analytics service - recieved messsage: {body}")
    
connection_parameters = pika.ConnectionParameters()
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_declare(exchange="routing", exchange_type=ExchangeType.direct)

queue = channel.queue_declare(queue="", exclusive=True)

channel.queue_bind(exchange="routing", queue=queue.method.queue, routing_key="analytics")

channel.basic_consume(queue=queue.method.queue, auto_ack=True, on_message_callback=message_recieved)

print("start consuming")

channel.start_consuming()