count = int(input())

for i in range(count):
    i = input()
    string = list(i)
    sum = 0
    count = 1
    for i in string:
        if i == 'O':
            sum += count
            count += 1
        else:
            count = 1
    print(sum)