import sys
sys.setrecursionlimit(1000000)
n, m, k = map(int, sys.stdin.readline().split())

graph = [[0] * (m+1) for _ in range(n+1)]
visited = [[0] * (m+1) for _ in range(n+1)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(k) :
    r, c = map(int, sys.stdin.readline().split())
    graph[r][c] = 1

def dfs(x,y) :
    global cnt
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 1 and ny >= 1 and nx <= n and ny <= m :
            if visited[nx][ny] == 0 and graph[nx][ny] == 1 :
                cnt += 1
                visited[nx][ny] = 1
                dfs(nx,ny)
answer = []
for i in range(1, n+1) :
    for j in range(1, m+1) :
        cnt = 0
        if graph[i][j] == 1 and visited[i][j] == 0 :
            dfs(i,j)
            answer.append(cnt)
print(max(answer))