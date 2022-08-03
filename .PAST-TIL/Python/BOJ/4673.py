num = set(range(1, 10001))
general = set()

for i in num:
    for j in str(i):
        i += int(j)
    general.add(i)

self_num = sorted(num - general)

for i in self_num:
    print(i)
