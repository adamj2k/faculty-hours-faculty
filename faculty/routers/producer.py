import pika

from faculty.settings import RABBITMQ_PASSWORD, RABBITMQ_USER

QUEUE_LIST = ["teacher-report-queue", "personal-report-queue", "summary-report-queue"]


def send_message(message, queue, teacher_id=None):
    """
    Send message to queue
    Parameters:
    - message: information about change
    - queue: name of queue - report to generate
    """
    if teacher_id == None:
        channel = declare_queue(queue)
        channel.basic_publish(exchange="", routing_key=queue, body=message)
        print(f" Generate report for '{message}'")
    else:
        send_teacher_id = " id=" + str(teacher_id)
        channel = declare_queue(queue)
        channel.basic_publish(
            exchange="", routing_key=queue, body=message + str(send_teacher_id)
        )
        print(f" Generate report for '{message}'")


def producer_connection():
    """
    Connection to rabbitmq server
    Return channel connection
    """
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            "faculty-hours-broker-rabbitmq-1",
            5672,
            "faculty-vhost",
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
