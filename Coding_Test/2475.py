n = list(map(int, input().split(" ")))

answer = 0
for i in n:
    answer += i**2

print(answer % 10)