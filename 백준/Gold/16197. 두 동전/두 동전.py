import sys
from collections import deque

n, m = map(int,sys.stdin.readline().split())

coin = deque()
board = []
temp = []
for i in range(n):
    board.append(list(input().strip()))
    for j in range(m):
        if board[i][j] == "o":
            temp.append((i, j))

coin.append((temp[0][0], temp[0][1], temp[1][0], temp[1][1], 0))

def bfs() :
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    while True :
        x1, y1, x2, y2, cnt = coin.popleft()
        if cnt >= 10 :
            return -1

        for i in range(4) :
            nx1 = x1 + dx[i]
            nx2 = x2 + dx[i]
            ny1 = y1 + dy[i]
            ny2 = y2 + dy[i]
            if 0 <= nx1 < n and 0 <= nx2 < n and 0 <= ny1 < m and 0 <= ny2 < m :
                if board[nx1][ny1] == '#' :
                    nx1, ny1 = x1, y1
                if board[nx2][ny2] == '#' :
                    nx2, ny2 = x2, y2
                coin.append((nx1, ny1, nx2, ny2, cnt + 1))
            elif 0 <= nx1 < n and 0 <= ny1 < m:  # coin2가 떨어진 경우
                return cnt + 1
            elif 0 <= nx2 < n and 0 <= ny2 < m:  # coin1가 떨어진 경우
                return cnt + 1
            else:  # 둘 다 빠진 경우 무시
                continue
print(bfs())