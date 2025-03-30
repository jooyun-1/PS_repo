import sys
from collections import deque
# O는 빈 공간, X는 벽, I는 도연이, P는 사람

n, m = map(int,sys.stdin.readline().split())
board = []
start = []
for i in range(n) :
    line = list(sys.stdin.readline().rstrip())
    for j in range(len(line)) :
        if 'I' == line[j] :
            start = [i,j]
    board.append(line)

def bfs(x,y) :
    que = deque()
    visited = [[0] * m for _ in range(n)]
    que.append([x,y])
    visited[x][y] = 1
    dx, dy = [1,-1,0,0], [0,0,1,-1]
    cnt = 0
    while que :
        x, y = que.popleft()
        if board[x][y] == 'P' :
            cnt += 1
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m :
                if visited[nx][ny] == 0 :
                    if board[nx][ny] == 'O' or board[nx][ny] == 'P' :
                        que.append([nx,ny])
                        visited[nx][ny] = 1
    return cnt
answer = bfs(start[0],start[1])
if answer == 0 :
    print('TT')
else :
    print(answer)