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
        else:
            print(arr[len(arr)-1])
            del arr[len(arr)-1]

    if command[0] == "size":
        print(len(arr))

    if command[0] == "empty":
        if len(arr) == 0:
            print(1)
        else:
            print(0)

    if command[0] == "top":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[len(arr)-1])