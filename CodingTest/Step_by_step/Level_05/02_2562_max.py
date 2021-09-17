numbers = []
for i in range(9):
    num = int(input())
    numbers.append(num)
print(max(numbers))
print(numbers.index(max(numbers))+1)