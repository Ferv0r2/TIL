def quaternion(i, j):
    if i > 0 and j > 0:
        return 1
    elif i < 0 and j > 0:
        return 2
    elif i < 0 and j < 0:
        return 3
    else:
        return 4

x = int(input())
y = int(input())

print(quaternion(x, y))