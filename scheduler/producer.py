import pika
import os


def get_connection(host):
    user = os.environ.get("RABBITMQ_USER", "admin")
    password = os.environ.get("RABBITMQ_PASS", "rabbitmq")

    credentials = pika.PlainCredentials(user, password)
    parameters = pika.ConnectionParameters(host=host, credentials=credentials)

    return pika.BlockingConnection(parameters)


def produce(channel, body):
    channel.queue_declare(queue='router_queue', durable=True)
    channel.basic_publish(
        exchange='',
        routing_key='router_queue',
        body=body
    )