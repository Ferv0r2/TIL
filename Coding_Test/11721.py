from math import ceil

s = input()

n = ceil(len(s) / 10)

for i in range(n):
    print(s[i*10:(i+1)*10])