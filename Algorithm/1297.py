d, h, w = map(int, input().split(" "))

ratio = d / ((h ** 2 + w ** 2) ** 0.5)
print(int(ratio * h), int(ratio * w))