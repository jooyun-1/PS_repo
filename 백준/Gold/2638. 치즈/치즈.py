import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
board = []
for i in range(n) :
    arr = list(map(int, sys.stdin.readline().split()))
    board.append(arr)
time = 0
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(i,j) :
    que = deque()
    que.append((i,j))
    visited[i][j] = 1
    while que :
        x, y = que.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m :
                if visited[nx][ny] == 0 and board[nx][ny] == 0 :
                    que.append((nx,ny))
                    visited[nx][ny] = 1
                elif board[nx][ny] == 1 :
                    visited[nx][ny] = visited[nx][ny] + 1
    

while True :
    visited=[[0 for _ in range(m)] for _ in range(n)]
    bfs(0,0)
    time += 1
    cnt = 0
    for i in range(n) :
        for j in range(m) :
            if visited[i][j] >= 2 :
                board[i][j] = 0
    for i in range(n) :
        for j in range(m) :
            if board[i][j] == 0 :
                cnt += 1
    if cnt == (n*m) :
        break
print(time)


