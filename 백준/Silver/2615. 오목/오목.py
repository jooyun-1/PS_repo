import sys

board = [list(map(int,sys.stdin.readline().split())) for _ in range(19)]
visited = [[0] * 19 for _ in range(19)]

dx = [0,1,1,-1]
dy = [1,0,1,1]

for x in range(19):
    for y in range(19):
        if board[x][y] != 0:

            for i in range(4):
                cnt = 1
                nx = x + dx[i]
                ny = y + dy[i]

                # while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == board[x][y]:
                while True :
                    if 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == board[x][y] :
                        cnt += 1
                        if cnt == 5:
                            if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and board[x - dx[i]][y - dy[i]] == board[x][y]:
                                break
                            if 0 <= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19 and board[nx + dx[i]][ny + dy[i]] == board[x][y]:
                                break

                            print(board[x][y])
                            print(x + 1, y + 1)
                            sys.exit(0)

                        nx += dx[i]
                        ny += dy[i]
                    else :
                        break

print(0)

