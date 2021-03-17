import json
import random
from datetime import datetime
import datetime as dt

from app import Section


def section_generator(schedule_data):
    course_list = schedule_data["courseList"]
    block_list = schedule_data["blockList"]
    section_list = []
    section = {}
    for block in block_list:
        i = 0
        while i < random.randint(4, 6):
            start_date = datetime.strptime(block["startDate"], '%Y-%m-%d')
            end_date = datetime.strptime(block["endDate"], '%Y-%m-%d')
            section["blockId"] = block["blockId"]
            section["courseId"] = random.choice(course_list)["courseId"]
            section["startDate"] = str((start_date + dt.timedelta(days=1)).date())
            section["endDate"] = str((end_date - dt.timedelta(days=1)).date())
            i += 1
            section_object = Section(course_id=section["courseId"],
                                     block_id=section["blockId"],
                                     start_date=section["startDate"],
                                     end_date=section["endDate"])
            section_list.append(section) 
    return section_list

