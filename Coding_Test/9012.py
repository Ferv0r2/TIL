import sys

n = int(sys.stdin.readline())

for i in range(n):
    result = "YES"
    ps = sys.stdin.readline()

    left = 0
    right = 0

    if ps[0] == ")":
        print("NO")
        continue
    if ps[len(ps)-1] == "(":
        print("NO")
        continue

    for c in ps:
        if c == "(":
            left += 1
        if c == ")":
            right += 1

        if right > left:
            result = "NO"
            break
    
    if left != right:
        result = "NO"
        
    print(result)