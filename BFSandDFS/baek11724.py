import sys
sys.setrecursionlimit(100000)

N, M = map(int,sys.stdin.readline().split())
graph = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 0
for i in range(M) :
    a, b = map(int,sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1

def dfs(node) :
    visited[node] = 1
    for i in range(1,N+1) :
        if visited[i] == 0 and graph[node][i] == 1 :
            dfs(i)

for i in range(1,N+1) :
    if visited[i] == 0 :
        dfs(i) 
        cnt += 1
print(cnt)