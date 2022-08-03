import sys

n = int(sys.stdin.readline())

arr = []
for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == "push":
        arr.append(command[1])

    if command[0] == "pop":
        if len(arr) == 0:
            print(-1)
            continue
        
        print(arr[0])
        del arr[0]
    
    if command[0] == "size":
        print(len(arr))

    if command[0] == "empty":
        print(1 if len(arr) == 0 else 0)

    if command[0] == "front":
        if len(arr) == 0:
            print(-1)
            continue

        print(arr[0])


    if command[0] == "back":
        if len(arr) == 0:
            print(-1)
            continue
        
        print(arr[len(arr)-1])