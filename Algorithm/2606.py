import sys

def dfs(start):
    global cnt
    visited[start] = 1
    for i in graph[start]:
        if visited[i]==0:
            dfs(i)
            cnt +=1

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[]*n for _ in range(n+1)]

for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
cnt = 0
visited = [0]*(n+1)

dfs(1)
print(cnt)