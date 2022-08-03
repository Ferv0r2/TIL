n, k = map(int, input().split())

arr = []
for i in range(n):
    arr.append(int(input()))

result = 0
for i in reversed(arr):
    result += k // i
    k = k % i

print(result)