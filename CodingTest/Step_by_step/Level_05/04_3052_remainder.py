numbers = []
count = 0
for i in range(10):
    n = int(input())
    numbers.append(n % 42)

for i in range(len(numbers)):
    if numbers[i] == numbers[i+1]:
        count = count + 1

print(count)