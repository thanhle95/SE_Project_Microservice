import datetime as dt
import random
from datetime import datetime


def section_generator(schedule_data):
    print(f"schedule_data {schedule_data}")
    course_list = schedule_data["course_list"]
    # print(course_list)
    block_list = schedule_data["block_list"]
    # print(block_list)
    section_list = []
    section = {}
    for block in block_list:
        i = 0
        while i < random.randint(4, 6):
            print("có vô đây nè")
            start_date = datetime.strptime(block["startDate"], '%Y-%m-%d')
            end_date = datetime.strptime(block["endDate"], '%Y-%m-%d')
            section["blockId"] = block["blockId"]
            course = random.choice(course_list)
            section["courseId"] = course["courseId"]
            section["startDate"] = str((start_date + dt.timedelta(days=1)).date())
            section["endDate"] = str((end_date - dt.timedelta(days=1)).date())
            section["capacity"] = course["courseCapacity"]
            i += 1

            section_list.append(section)

    print(section_list)
    return section_list

