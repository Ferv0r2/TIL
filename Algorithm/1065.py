def hansu(x):
    x = str(x)
    d = int(x[1]) - int(x[0])

    for i in range(len(x)-1):
        if int(x[i+1]) != int(x[i]) + d:
            return False

    return True


n = int(input())

result = 0
for i in range(1, n+1):
    if i < 100:
        result += 1
        continue

    if hansu(i):
        result += 1

print(result)