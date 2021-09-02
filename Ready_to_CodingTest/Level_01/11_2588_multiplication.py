a = input()
b = input()

sum = 0
digit = 0

for i in map(int, str(b)[::-1]):
    amount = int(a) * i
    print(amount)
    sum += amount * ( 10 ** digit )
    digit += 1

print(sum)