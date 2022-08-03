count = int(input())
score = list(map(int, input().split()))

max_num = max(score)
amount = 0

for i in range(count):
    if score[i] == max_num:
        pass
    amount += score[i]/max_num * 100

print(amount/count)