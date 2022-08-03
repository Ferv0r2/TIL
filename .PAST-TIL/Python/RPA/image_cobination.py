import random
import json
import sys
import pandas as pd
from PIL import Image

bg_list, pattern_list, eyebrows_list, head_list, \
    eyes_list, neck_list, mouse_list = [], [], [], [], [], [], []

path = ['PixelDogeClub Background', 'PixelDogeClub Pattern', 'PixelDogeClub Eyebrows',
        'PixelDogeClub Head', 'PixelDogeClub Eyes', 'PixelDogeClub Neck', 'PixelDogeClub Mouse']

# 원하는 갯수
print('시작 갯수, 끝 갯수 입력')
start, end = map(int, sys.stdin.readline().split())

line = Image.open("pixel/line.png")
base = Image.open("pixel/base.png")

for i in range(10):
    bg = Image.open(f"pixel/{path[0]}/background_{i}.png")
    pattern = Image.open(f"pixel/{path[1]}/pattern_{i}.png")
    eyebrows = Image.open(f"pixel/{path[2]}/eyebrows_{i}.png")
    head = Image.open(f"pixel/{path[3]}/head_{i}.png")
    eyes = Image.open(f"pixel/{path[4]}/eyes_{i}.png")
    neck = Image.open(f"pixel/{path[5]}/neck_{i}.png")
    mouse = Image.open(f"pixel/{path[6]}/mouse_{i}.png")

    bg_list.append(bg)
    pattern_list.append(pattern)
    eyebrows_list.append(eyebrows)
    head_list.append(head)
    eyes_list.append(eyes)
    neck_list.append(neck)
    mouse_list.append(mouse)


ran_list = []
ran_list.append([3, 1, 6, 3, 5, 10, 4])  # 0000번 사전등록

for i in range(start, end+1):
    new_random = []
    ran = [0] * len(path)

    for j in range(len(ran)):
        ran[j] = random.randrange(10)
        new_random.append(ran[j])

    while new_random in ran_list:
        new_random = []

        ran = [0] * len(path)

        for j in range(len(ran)):
            ran[j] = random.randrange(10)
            new_random.append(ran[j])

    ran_list.append(new_random)

    base.paste(bg_list[ran[0]], mask=bg_list[ran[0]])
    base.paste(pattern_list[ran[1]], mask=pattern_list[ran[1]])
    base.paste(line, mask=line)
    base.paste(eyebrows_list[ran[2]], mask=eyebrows_list[ran[2]])
    base.paste(head_list[ran[3]], mask=head_list[ran[3]])
    base.paste(eyes_list[ran[4]], mask=eyes_list[ran[4]])
    base.paste(neck_list[ran[5]], mask=neck_list[ran[5]])
    base.paste(mouse_list[ran[6]], mask=mouse_list[ran[6]])

    base.save('./Completed_v3/DOGE FRIENDS #%04d.png' % i, 'PNG')\



item_counts_list = []
for i in range(len(path)):
    item_counts = [0] * 10
    for j in range(len(ran_list)):
        index = ran_list[j][i] - 1
        item_counts[index] += 1
    item_counts_list.append(item_counts)


value = {'Background': item_counts_list[0],
         'Pattern': item_counts_list[1],
         'Eyebrows': item_counts_list[2],
         'Head': item_counts_list[3],
         'Eyes': item_counts_list[4],
         'Neck': item_counts_list[5],
         'Mouse': item_counts_list[6]}

value = pd.DataFrame(value)

value.to_excel(excel_writer='./excel/2021_10_22.xlsx')
