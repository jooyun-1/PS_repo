import sys
from collections import deque

m, n = map(int,sys.stdin.readline().split())
graph = []
day = 0
dx = [1,-1,0,0]
dy = [0,0,1,-1]
que = deque()
for i in range(n) :
    line = list(map(int,sys.stdin.readline().split()))
    graph.append(line)

for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 1 :
            que.append([i,j])

def bfs() :
    while que :
        x, y = que.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < n and ny < m :
                if graph[nx][ny] == 0 :
                    graph[nx][ny] = graph[x][y] + 1
                    que.append([nx,ny])

bfs()
for i in graph :
    for j in i :
        if j == 0 :
            print(-1)
            exit(0)
    day = max(day,max(i))
print(day-1)