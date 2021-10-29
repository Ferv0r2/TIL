text = ""

on_time = '오후 9:00'

with open("텍스트파일.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

    for line in lines[5:]:
        if '] [' in line:
            if on_time in line:
                text+=line

print(text)