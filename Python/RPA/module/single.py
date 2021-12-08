import random, pandas as pd

# 최초 리스팅 단계
try: # 변경 파일 있으면 가져오고
    seeds = pd.read_excel('./module/changing.xlsx', usecols=['type'])
    count = pd.read_excel('./module/changing.xlsx', usecols=['count'])
    seeds_list = seeds.values.tolist()
    count = count.loc[0].tolist()
    count = int(float(str(count)[1:-1]))

except: # 없으면 1렙으로 새로 생성
    seeds = pd.read_excel('./module/sp.xlsx', usecols=['a'])
    count = pd.read_excel('./module/sp.xlsx', usecols=['b'])
    seeds_list = seeds.values.tolist()
    count = count.loc[0].tolist()
    count = int(float(str(count)[1:-1]))

# 랜덤 추첨
upgrade = []
size = len(seeds_list)
time = 0
for i in seeds_list:
    if time == size - 1:
        break

    ran = random.randrange(10) # 10개 중 1개의 확률 추출 -> 10퍼
    if ran == 1: # 해당 숫자 레벨업
        upgrade.append(time)
        if i == [1]:
            seeds_list[time] = [2]
            print('새싹!', end=" ")
            continue

        elif i == [2]:
            seeds_list[time] = [3]
            print('꽃 피었다', end=" ")
            continue

        elif i == [3]:
            seeds_list[time] = [4]
            print('열매 등장', end=" ")
            continue

        elif i == [4]: # 누구걸지를 고려하진 않음
            seeds_list[time] = [3]
            if time == 0 or time == 1 or time == 2: # 레어
                seeds_list.append([1]) 
                seeds_list.append([1]) 
                seeds_list.append([1]) 
                print('로켓단 등장', end=" ")
        
            elif time == 3 or time == 4 or time == 5 \
                or time == 6 or time == 7 or time == 8 \
                or time == 9 or time == 10 or time == 11 or time == 12: # 준 레어
                seeds_list.append([1]) 
                seeds_list.append([1]) 
                print('쌍둥이 탄생', end=" ")
        
            else:
                seeds_list.append([1]) 
                print('새 생명 탄생', end=" ")
            continue
        continue
    time += 1
        


# print (seeds_list)


# 리스트 형식 제거
item = ""
item_list = []
for i in range(len(seeds_list)):
    item = str(seeds_list[i])[1:-1]
    item_list.append(int(item))

print('\n선택받은 친구들 : ', upgrade)
print('선택받은 친구들 수 : ', len(upgrade))
print('총 SP 수 : ', len(seeds_list))
print('작업 횟수 : ', count+1)
print('===정렬 시켰을 때===\n', item_list)

try:
    value = {'type':item_list,
            'count': count+1}

except:
    value = {'type':item_list,
            'count': 0}

value = pd.DataFrame(value)

value.to_excel(excel_writer='./module/changing.xlsx')
