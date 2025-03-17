import pika
from pika.exchange_type import ExchangeType

def on_message1_recieved(ch, method, properties, body):
    print(f"recieved message from 1: {body}")
    
def on_message2_recieved(ch, method, properties, body):
    print(f"recieved message from 2: {body}")
    
connection_parameters = pika.ConnectionParameters()
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_declare("simplehash", "x-consistent-hash")

channel.queue_declare(queue="letterbox1")
channel.queue_bind("letterbox1", "simplehash", routing_key='1')
channel.basic_consume(queue="letterbox1", auto_ack=True, on_message_callback=on_message1_recieved)

channel.queue_declare(queue="letterbox2")
channel.queue_bind("letterbox2", "simplehash", routing_key='4')
channel.basic_consume(queue="letterbox2", auto_ack=True, on_message_callback=on_message2_recieved)

print("start consuming")

channel.start_consuming()