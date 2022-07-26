import sys

def fibonacci(n):
    if len(zero) <= n:
        for i in range(len(zero), n+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print(zero[n], one[n])

t = int(sys.stdin.readline())
zero = [1, 0, 1]
one = [0, 1, 1]


for i in range(t):
    num = int(sys.stdin.readline())
    fibonacci(num)