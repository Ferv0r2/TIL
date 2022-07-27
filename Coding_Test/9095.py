import sys

def isSum(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    elif x == 3:
        return 4
    else:
        return isSum(x-1) + isSum(x-2) + isSum(x-3)

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())

    print(isSum(n))