amount = 0
for i in list(map(int, input().split())):
    amount += i**2

print(amount%10)


# a, b, c, d, e = list(map(int, input().split()))

# amount = a**2 + b**2 + c**2 + d**2 + e**2
# print(amount%10)