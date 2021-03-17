import pika, json
from datetime import datetime

import schedule_generator
from app import Section, db

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
    # print(" [x] Received %r" % body)
    data = json.loads(body)
    print(type(data))

    section_list = schedule_generator.section_generator(data)

    for section in section_list:
        print("helllooo worrlddddddddd")
        section_object = Section(course_id=section["courseId"],
                                 block_id=section["blockId"],
                                 start_date=section["startDate"],
                                 end_date=section["endDate"],
                                 capacity=section["capacity"])
        db.session.add(section_object)
        db.session.commit()
    section = Section.query.all()
    for sec in section:
        print(sec.course_id)
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

    channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()

    channel.close()


if __name__ == '__main__':
    subcribe()