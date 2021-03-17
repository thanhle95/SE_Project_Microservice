import pika
from datetime import datetime

host = "host.docker.internal"
port = 5672
username = "guest"
password = "guest"
queue = "builder"
virtualhost = "/"
heartbeat = 600


def rabbitmq_connector():
    admin_credentials = pika.PlainCredentials(username, password)

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=host, port=port, virtual_host=virtualhost,
                                  credentials=admin_credentials, heartbeat=heartbeat))
    channel = connection.channel()
    return channel


def callback(ch, method, properties, body):
    # data = json.load(body)
    print(" [x] Received %r" % body)
    # print(data)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    f = open("mess.txt", "w")
    print(type(current_time))
    f.writelines(f" %r {current_time}" % body)
    f.close()

    if properties.content_type == 'schedule_generator':
        pass

    elif properties.content_type == 'get_schedule':
        pass


def publish(messages):
    channel = rabbitmq_connector()

    channel.basic_publish(exchange="", routing_key="", queue="", messages=messages)
    return None


def subcribe():
    channel = rabbitmq_connector()

    print(' [*] Waiting for messages. To exit press CTRL+C')

    channel.basic_consume(queue=queue, on_message_callback=callback)

    channel.start_consuming()
