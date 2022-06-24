# count = int(input())

# for i in range(count):
#     amount, value = 0, 0
#     score = list(map(int, input().split()))

#     for j in range(score[0]+1):
#         if j != 0:
#             amount += score[j]
    
#     average = amount/score[0]
#     for k in range(score[0]+1):
#         if k != 0:
#             if score[k] > average:
#                 value += 1
    
#     final = round((value/score[0])*100, 3)
#     print(f'{final:.3f}%')

n = int(input())

for _ in range(n):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:])/nums[0]  # 평균을 구함 (nums[0]: 학생수, nums[1:] 점수)
    cnt = 0
    for score in nums[1:]:
        if score > avg:
            cnt += 1  # 평균 이상인 학생 수
    rate = cnt/nums[0] *100
    print(f'{rate:.3f}%')