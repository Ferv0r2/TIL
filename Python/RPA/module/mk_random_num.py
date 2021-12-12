import random, pandas as pd

size = 100
num_list = []

for i in range(size):
    num = random.randrange(size)
    if num in num_list:
        while True:
            num = random.randrange(size)
            if num not in num_list:
                break
    num_list.append(num)
    print(i)


raw_data = {'gacha_num' : num_list }
raw_data = pd.DataFrame(raw_data) #데이터 프레임으로 전환
raw_data.to_excel(excel_writer='gacha_number_test.xlsx') #엑셀로 저장