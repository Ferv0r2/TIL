import sys

n = int(sys.stdin.readline())
data = [0] * 1000001

for i in range(2, n+1):
    data[i] = data[i-1] + 1

    if i % 3 == 0:
        data[i] = min(data[i], data[i//3] + 1)

    if i % 2 == 0:
        data[i] = min(data[i], data[i//2] + 1)

print(data[n])