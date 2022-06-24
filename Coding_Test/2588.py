a = int(input())
b = input()

answer = 0
for i in range(len(b)):
    print(a * int(b[len(b) - 1 - i]))

print(a * int(b))