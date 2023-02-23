import sys
sys.setrecursionlimit(100000) # 파이썬에서는 1000번이상의 recursion이 발생하면 error 뜸

def dfs(x, y) :
    if x >= N or y >= M or y < 0 or x < 0 :
        return
    if visited[x][y] == 0 and graph[x][y] == 1 :
        visited[x][y] = 1
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx,ny)

T = int(input())
answer = []

for t in range(T) :
    M, N, K = map(int, input().split())
    graph = [[0] * (M) for i in range(N)]
    visited = [[0] * (M) for i in range(N)]
    cnt = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(K) :
        x, y = map(int, input().split())
        graph[y][x] = 1

    for i in range(N) :
        for j in range(M) :
            if graph[i][j] == 1 and visited[i][j] == 0 :
                cnt += 1
                dfs(i,j)
    answer.append(cnt)

for ans in answer :
    print(ans)
