numbers = []
for i in range(10):
    n = int(input())
    num = n % 42
    if numbers.count(num) == 0:
        numbers.append(n % 42)

print(len(numbers))