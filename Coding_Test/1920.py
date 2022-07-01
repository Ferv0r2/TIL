import sys

n = sys.stdin.readline()
x = set(sys.stdin.readline().split())
m = sys.stdin.readline()
y = sys.stdin.readline().split()

for c in y:
    print(1) if c in x else print(0)