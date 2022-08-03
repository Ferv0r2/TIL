import sys

n = int(input())
for i in range(n):
    a, b = list(map(int, sys.stdin.readline().split()))
    print(a+b)