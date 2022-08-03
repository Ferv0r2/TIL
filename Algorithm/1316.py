def group(w):
    arr = [0] * 26
    for s in w:
        arr[ord(s)-97] += 1
        
    if max(arr) == 1:
        return True

    for i in range(26):
        if arr[i] >= 2:
            if chr(i+97) * arr[i] not in w:
                return False

    return True

n = int(input())
result = 0

for i in range(n):
    word = input()

    if group(word):
        result += 1

print(result)