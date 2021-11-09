from enum import Enum

class Day(Enum):
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
       
class Class(Enum):
    first_class = 1 # 0955 ~ 1045
    second_class = 2 # 1050 ~ 1140
    third_class = 3 # 1145 ~ 1235
    fourth_class = 4 # 1240 ~ 1330
    fifth_class = 5 # 1335 ~ 1425
    sixth_class = 6 # 1430 ~ 1520
    seventh_class = 7 # 1525 ~ 1615

class Lecture:
    def __init__(self, lecture_name, professor, start_class, class_time, lecture_day):
        self.lecture_name = lecture_name
        self.professor = professor
        self.start_class = start_class
        self.class_time = class_time
        self.lecture_day = lecture_day

class Timetable:
    def __init__(self, lecture_name, professor, start_class, class_time, lecture_day):
        self.lecture_name = lecture_name
        self.professor = professor
        self.start_class = start_class
        self.class_time = class_time
        self.lecture_day = lecture_day



# main