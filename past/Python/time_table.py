class Lecture:
    def __init__(self, lecture_name, professor):
        self.lecture_name = lecture_name
        self.professor = professor

class Timetable:
    def __init__(self, lecture_name, professor, start_class, end_class, lecture_day):
        self.lecture_name = lecture_name
        self.professor = professor
        self.start_class = start_class
        self.end_class = end_class
        self.lecture_day = lecture_day

    def show(self):
        print("==============================\n")
        print("강의명 : ", self.lecture_name)
        print("교수명 : ", self.professor)
        print("시작시간 : ", self.start_class)
        print("끝시간 : ", self.end_class)
        print("강의요일 : ", self.lecture_day)
        print("\n==============================")
       

day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]       
time = [
    "first_class", # 0900 ~ 0950
    "second_class", # 0955 ~ 1045
    "third_class", # 1050 ~ 1140
    "fourth_class", # 1145 ~ 1235
    "fifth_class", # 1240 ~ 1330
    "sixth_class", # 1335 ~ 1425
    "seventh_class", # 1430 ~ 1520
    "eighth_class" # 1525 ~ 1615
]

# main
Lecture_list = [
    Lecture("프로젝트패키징", "이용희"),
    Lecture("빅데이터", "양숙희"),
    Lecture("IT영어이해", "장종준"),
    Lecture("프로젝트패키징", "이용희"),
    Lecture("프레젠테이션실습", "정미아"),
    Lecture("IoT응용기술", "정세일")
]

황원태 = [
    Timetable(Lecture_list[0].lecture_name, Lecture_list[0].professor, time[1], time[4], day[0]),
    Timetable(Lecture_list[1].lecture_name, Lecture_list[1].professor, time[1], time[4], day[1]),
    Timetable(Lecture_list[2].lecture_name, Lecture_list[2].professor, time[5], time[7], day[1]),
    Timetable(Lecture_list[3].lecture_name, Lecture_list[3].professor, time[1], time[4], day[2]),
    Timetable(Lecture_list[4].lecture_name, Lecture_list[4].professor, time[1], time[4], day[3]),
    Timetable(Lecture_list[5].lecture_name, Lecture_list[5].professor, time[5], time[7], day[3])
]

while True:
    value = 0
    print("항목을 선택하세요.")
    print("1: 교수명 검색 2: 요일 검색 0: 종료")
    num = int(input())

    if num == 0:
        break

    elif num == 1:
        search = input("특정 교수명 검색 : ")

        for lec in 황원태:
            if search == lec.professor:
                lec.show()
                value += 1
        if value == 0:
            print("해당 값이 없습니다.")

    elif num == 2:
        search = input("특정 요일 검색 : ")

        for lec in 황원태:
            if search == lec.lecture_day:
                lec.show()
                value += 1
        if value == 0:
            print("해당 값이 없습니다.")

    
