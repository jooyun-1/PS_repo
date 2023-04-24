import sys
n, m = map(int, sys.stdin.readline().split())

miro = [[0] * (m+1) for _ in range(n+1)]
visited = [[0] * (m+1) for _ in range(n+1)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(n) :
    line = sys.stdin.readline().rstrip()
    for j in range(len(line)) :
        miro[i+1][j+1] = int(line[j])

def bfs(x,y) :
    que = list()
    que.append([x,y])
    visited[x][y] = 1

    while que :
        x, y = que.pop(0)

        if x == n and y == m :
            print(visited[x][y])
            break
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 1 and ny >=1 and nx <= n and ny <= m :
                if visited[nx][ny] == 0 and miro[nx][ny] == 1 :
                    que.append([nx,ny])
                    visited[nx][ny] = visited[x][y] + 1

bfs(1,1)