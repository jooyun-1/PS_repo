import sys
from collections import deque

M, N, H = map(int,sys.stdin.readline().split())
board = [[list(map(int,sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]
que = deque()

def bfs() :
    while que :
        z, x, y = que.popleft()
        for i in range(6) :
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H :
                if board[nz][nx][ny] == 0 :
                    board[nz][nx][ny] = board[z][x][y] + 1
                    que.append((nz,nx,ny))

for i in range(H) :
    for j in range(N) :
        for k in range(M) :
            if board[i][j][k] == 1 :
                que.append((i,j,k))
bfs()

flag = False
answer = 0

for i in range(H) :
    for j in range(N) :
        for k in range(M) :
            if board[i][j][k] == 0 :            
                flag = True
            answer = max(answer, board[i][j][k])
if flag :
    print(-1)
else :
    print(answer-1)