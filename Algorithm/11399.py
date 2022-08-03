n = int(input())

tm = map(int, input().split())

result = 0
tmp = 0
for i in sorted(tm):
    tmp += i
    result += tmp

print(result)