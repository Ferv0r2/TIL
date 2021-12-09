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

upgrade = []
for i in range(30):
    size = len(seeds_list)
    time = 0
    for i in seeds_list:
        if time == size - 1:
            break

        ran = random.randrange(10) # 10개 중 1개의 확률 추출 -> 10퍼
        if ran == 1: # 해당 숫자 
            if time not in upgrade:
                upgrade.append(time)
            if i == [1]:
                seeds_list[time] = [2]
                print('새싹몬 진화!', end=" ")
                continue

            if i == [2]:
                seeds_list[time] = [3]
                print('꽃이 피었다구욧', end=" ")
                continue

            if i == [3]:
                seeds_list[time] = [4]
                print('열매 두둥등장', end=" ")
                continue

            if i == [4]: # 누구걸지를 고려하진 않음
                seeds_list[time] = [3]
                if time < 3: # 레어
                    seeds_list.append([1]) 
                    seeds_list.append([1]) 
                    seeds_list.append([1]) 
                    print('로켓단 등장', end=" ")
        
                if time >= 3 and time < 13: # 준 레어
                    seeds_list.append([1]) 
                    seeds_list.append([1]) 
                    print('쌍둥이가 탄생했다 이말이야', end=" ")
        
                if time >= 13:
                    seeds_list.append([1]) 
                    print('새 생명이 탄생했다 이말이야', end=" ")
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
            'count': count+30}

except:
    value = {'type':item_list,
            'count': 0}

value = pd.DataFrame(value)

value.to_excel(excel_writer='./module/changing.xlsx')
