n = int(input())

for i in range(n):
    s = input()

    answer = ""
    for c in s:
        if c == "Z":
            answer += "A"
        else:
            answer += chr(ord(c)+1)
    
    print(f"String #{i+1}")
    print(answer)
    print()