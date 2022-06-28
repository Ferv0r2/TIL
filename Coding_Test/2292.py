n = int(input())

hive = 1
cnt = 1

while n > hive:
    hive += 6 * cnt
    cnt += 1

print(cnt)