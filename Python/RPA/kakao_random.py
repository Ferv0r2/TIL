import random

text = ""
string_list = []
new_list = []
final_list = []
index = 0

# num = input('날짜 입력')
day = '--------------- 2021년 10월 28일 목요일 ---------------\n'
on_time = '오후 9:00'

with open("텍스트파일.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

    for line in lines[5:]:
        if day in line:
            string_list.append(line)
        if '] [' in line:
            if on_time in line:
                string_list.append(line)

start = string_list.index(day)

new_list = string_list[start+1:]

for i in range(len(new_list)):
    text = ""
    for j in new_list[i]:
        text += j
        if j == ']':
            break
    new_list[i] = text

for i in range(len(new_list)):
    if new_list[i] not in final_list:
        final_list.append(new_list[i])

final_list.remove('[PixelDogeClub]')

ran = random.randrange(len(final_list))

print("===== 추첨 명단 =====")
print(final_list)
print("===== 당첨자 =====")
print(final_list[ran])