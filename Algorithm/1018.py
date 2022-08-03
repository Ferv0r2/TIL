import sys

def counter(x, y):
    if x < 0 or x > n - 8 or y < 0 or y > m - 8:
        return False

    current = ["W", "B"]
    count = [0] * 2
    index = 0

    for i in range(x, x+8):
        for j in range(y, y+8):
            if i % 2 == 0:
                if j % 2 == 0:
                    index = 0
                else:
                    index = 1

            else:
                if j % 2 == 0:
                    index = 1
                else:
                    index = 0

            if board[i][j] != current[index]:
                count[0] += 1

    for i in range(x, x+8):
        for j in range(y, y+8):
            if i % 2 == 0:
                if j % 2 == 0:
                    index = 1
                else:
                    index = 0

            else:
                if j % 2 == 0:
                    index = 0
                else:
                    index = 1

            if board[i][j] != current[index]:
                count[1] += 1

    return count

n, m = map(int, sys.stdin.readline().split())

board = []
for i in range(n):
    board.append(sys.stdin.readline())

result = n * m
for i in range(n):
    for j in range(m):
        tmp = []
        tmp = counter(i, j)

        if tmp:
            result = min(result, tmp[0], tmp[1])

print(result)