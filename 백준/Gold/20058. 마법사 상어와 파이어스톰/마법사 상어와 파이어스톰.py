import sys

N, Q = map(int,sys.stdin.readline().split())
board = []
for n in range(2**N) :
    line = list(map(int,sys.stdin.readline().split()))
    board.append(line)
L_arr = list(map(int,sys.stdin.readline().split()))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for l in L_arr:
    # 1. 회전하기
    rotate_board = [[0] * (2 ** N) for _ in range(2 ** N)]
    for i in range(0, 2 ** N, 2 ** l):
        for j in range(0, 2 ** N, 2 ** l):
            for i2 in range(2 ** l):
                for j2 in range(2 ** l):
                    # 회전 후 행 위치 = 회전 전 열 위치
                    # 회전 후 열 위치 = N - 회전 전 행 위치 - 1
                    rotate_board[i + j2][j + 2 ** l - i2 - 1] = board[i + i2][j + j2]
    # 2. 얼음 녹이기
    board = [[0] * (2 ** N) for _ in range(2 ** N)]
    for x in range(2**N) :
        for y in range(2**N) :
            cnt = 0
            for i in range(4) :
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < 2**N and 0 <= ny < 2**N and rotate_board[nx][ny] != 0 :
                    cnt += 1
            if rotate_board[x][y] != 0 :
                if cnt < 3 :
                    board[x][y] = rotate_board[x][y] - 1
                else :
                    board[x][y] = rotate_board[x][y]
# 3. 남아있는 얼음의 합
ice_sum = 0
visited = [[0]*(2**N) for _ in range(2**N)]
total = 0
for x in range(2**N) :
    for y in range(2**N) :
        if board[x][y] != 0 and visited[x][y] == 0 :
            que = []
            visited[x][y] = 1
            ice_sum += board[x][y]
            temp = 1
            que.append([x,y])
            while que :
                a, b = que.pop(0)
                for i in range(4) :
                    nx = a + dx[i]
                    ny = b + dy[i]
                    if 0 <= nx < 2**N and 0 <= ny < 2**N and board[nx][ny] != 0:
                        if visited[nx][ny] == 0 :
                            visited[nx][ny] = 1
                            ice_sum += board[nx][ny]
                            temp += 1
                            que.append([nx,ny])
            total = max(temp,total)
print(ice_sum)
print(total)