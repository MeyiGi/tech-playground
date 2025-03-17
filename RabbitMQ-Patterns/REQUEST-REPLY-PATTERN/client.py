import pika
import uuid

def on_reply_message_recieved(ch, method, properties, body):
    print(f"reply recieved: {body}")

connection_parameters = pika.ConnectionParameters()
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

reply_queue = channel.queue_declare(queue="", exclusive=True)

channel.basic_consume(queue=reply_queue.method.queue, auto_ack=True, on_message_callback=on_reply_message_recieved)

channel.queue_declare(queue="request-queue")

message = "Can I request a reply?"

cor_id = str(uuid.uuid4())

print(f"sending reqeust: {cor_id}")

channel.basic_publish(
    exchange="", 
    routing_key="request-queue", 
    properties=pika.BasicProperties(
        reply_to=reply_queue.method.queue,
        correlation_id=cor_id,
    ),
    body=message
)

print("Start client")

channel.start_consuming()