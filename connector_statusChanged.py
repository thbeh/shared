import os
import pika
import sys
import json

from pika.exceptions import AMQPConnectionError

oceanApiUser = "APIACCESS-2172"
oceanApiPassword = "STZ16QWpvjBSfdx4y72QkRZmsUU9HR3e"

oceanApiHostname = "stage-meridian.etrel.com" #"meridian.etrel.com"

amqp = f"amqps://{oceanApiUser}:{oceanApiPassword}@{oceanApiHostname}:5671/%2F"

parameters = pika.URLParameters(f'amqps://{oceanApiUser}:{oceanApiPassword}@{oceanApiHostname}:5671/%2F')


connection = pika.BlockingConnection(parameters)
channel = connection.channel()


#channel.queue_declare(queue=f"{oceanApiUser}.*.connector.statusChanged")

def callback(ch, method, properties, body):
    data = json.loads(body)
    #print(f" [x] Received {body.decode()}")
    print(data)

channel.basic_consume(queue=f'{oceanApiUser}.*.connector.statusChanged', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()


