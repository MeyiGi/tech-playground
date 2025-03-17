import pika

def on_request_message_recieved(ch, method, properties, body):
    print(f"request message {properties.correlation_id}")
    
    reply = "No, You can't request a reply"
    
    print(str(body))
    
    if str(body) == "b'Can I request a reply?'":
        reply = "Yes, You can request a reply"
    
    ch.basic_publish("", routing_key=properties.reply_to, body=reply)

connection_parameters = pika.ConnectionParameters()
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.queue_declare(queue="request-queue")

message = "Hello world!"

channel.basic_consume(queue="request-queue", auto_ack=True, on_message_callback=on_request_message_recieved)

print(f"starting server")

channel.start_consuming()