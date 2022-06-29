import sys

n = int(sys.stdin.readline())

arr = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    arr.append([x, y])

for i in sorted(arr):
    print(*i)
