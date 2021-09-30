a = [1, 1, 2, 2, 2, 8]
index = 0
for i in list(map(int, input().split())):
    print(a[index] - i, end=' ')
    index += 1