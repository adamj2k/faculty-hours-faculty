import pika

from faculty.settings import RABBITMQ_HOST, RABBITMQ_PASSWORD, RABBITMQ_USER


def send_message(message, queue):
    """
    Send message to queue
    """
    channel = declare_queue(queue)
    channel.basic_publish(exchange="", routing_key=queue, body=message)
    print(f" Generate report for '{message}'")


def producer_connection(queue):
    """
    Connection to rabbitmq server
    Return channel connection
    """
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            RABBITMQ_HOST,
            5672,
            "/",
            pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASSWORD),
        )
    )
    channel = connection.channel()
    return channel


def declare_queue(queue):
    """
    Declaring queue
    return channel with declared queue
    """
    channel = producer_connection()
    channel.queue_declare(queue=queue, durable=True)
    return channel
