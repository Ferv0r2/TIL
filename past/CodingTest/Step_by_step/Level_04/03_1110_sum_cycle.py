n = int(input())

aim = n
new_num, temp, answer = 0, 0, 0

while True:
    temp = n // 10 + n % 10
    new_num = (n%10) * 10 + temp % 10
    answer = answer + 1
    n = new_num
    if new_num == aim:
        break

print(answer)