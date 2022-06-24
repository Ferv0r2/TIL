n = list(map(int, input().split(" ")))

base = [1, 1, 2, 2, 2, 8]

for i in range(len(n)):
    print(base[i] - n[i], end=" ")