
def prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False

    return True


n = int(input())
arr = map(int, input().split())

result = 0
for num in arr:
    if num == 1:
        continue

    if prime(num):
        result += 1

print(result)