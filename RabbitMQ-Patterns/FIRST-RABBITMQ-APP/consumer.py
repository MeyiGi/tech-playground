import pika


def on_message_callback(ch, method, properties, body):
    print(f"recieved messeage: {body}")


connections_parameters = pika.ConnectionParameters()

connection = pika.BlockingConnection(connections_parameters)

channel = connection.channel()

channel.queue_declare("letterbox")

channel.basic_consume(queue="letterbox", auto_ack=True, on_message_callback=on_message_callback)

print("starting consuming")

channel.start_consuming()