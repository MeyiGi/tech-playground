import pika
import time
import random

def on_message_recieved(ch, method,properies, body):
    process_time = random.randint(1, 6)    
    print(f"received: {body}, processing will take {time}")
    time.sleep(process_time)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print("Finished processing")
    
connection_parameters = pika.ConnectionParameters("localhost")
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()


channel.queue_declare(queue="letterbox", durable=True)

channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue="letterbox", on_message_callback=on_message_recieved)

print("Starting Consuming")
channel.start_consuming()