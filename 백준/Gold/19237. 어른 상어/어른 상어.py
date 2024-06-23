import sys
import copy

N, M, k = map(int,sys.stdin.readline().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
board = []
for n in range(N) :
    board.append(list(map(int,sys.stdin.readline().split())))

directions = list(map(int,sys.stdin.readline().split()))

priority_arr = []
for i in range(M):
    temp = []
    for _ in range(4):
        temp.append(list(map(int, input().split())))
    priority_arr.append(temp)

smells = [[[0,0]] * N for _ in range(N)]

def update_smell() : # 1초당 냄새 갱신
    for i in range(N) :
        for j in range(N) :
            # 냄새가 남은 경우
            if smells[i][j][1] > 0 :
                smells[i][j][1] -= 1 
            # 상어가 있는 곳
            if board[i][j] != 0 :
                smells[i][j] = [board[i][j],k]

def move() :
    new_board = [[0] * N for _ in range(N)]
    for x in range(N) :
        for y in range(N) :
            if board[x][y] != 0 :
                dir = directions[board[x][y] - 1] # 바라보는 방향
                flag = False
                for i in priority_arr[board[x][y]-1][dir-1] : # 상어번호, 그 방향의 우선순위
                    nx = x + dx[i-1]
                    ny = y + dy[i-1]
                    if 0 <= nx < N and 0 <= ny < N :
                        if smells[nx][ny][1] == 0 :
                            # 바라보는 방향 바꾸기
                            directions[board[x][y]-1] = i
                            # 상어 이동
                            if new_board[nx][ny] == 0 :
                                new_board[nx][ny] = board[x][y]
                            else :
                                # 상어 번호 최소만 살음
                                new_board[nx][ny] = min(board[x][y],new_board[nx][ny])
                            flag = True
                            break
                if flag :
                    continue
                for i in priority_arr[board[x][y] - 1][dir - 1] : # 주변에 냄새가 모두 있으면
                    nx = x + dx[i-1]
                    ny = y + dy[i-1]
                    if 0 <= nx < N and 0 <= ny < N :
                        if smells[nx][ny][0] == board[x][y] :
                            # 상어가 바라보는 방향
                            directions[board[x][y] - 1] = i
                            # 상어 이동
                            new_board[nx][ny] = board[x][y]
                            break
    return new_board

time = 0
while True :
    update_smell()
    new_board = move()
    board = new_board # 진짜 board 갱신
    time += 1

    check = True
    for i in range(N) :
        for j in range(N) :
            if board[i][j] > 1 : # 상어 번호 1보다 큰 것이 있으면
                check = False

    if check :
        print(time)
        break
    if time >= 1000 :
        print(-1)
        break