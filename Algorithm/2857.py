answer = []

for i in range(1, 6):
    s = input()
    if "FBI" in s:
        answer.append(i)

if answer:
    print(*answer)
else:
    print("HE GOT AWAY!")