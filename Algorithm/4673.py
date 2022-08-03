n = set(range(1, 10000))
remover = set()
for num in n :
    for i in str(num):
        num += int(i)
    remover.add(num)

self_numbers = n - remover
for self_num in sorted(self_numbers):
    print(self_num)