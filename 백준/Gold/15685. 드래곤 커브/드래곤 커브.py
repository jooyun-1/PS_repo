import sys

N = int(sys.stdin.readline())
dir = [0,1,2,3] # 우, 상, 왼, 하
dx = [1,0,-1,0]
dy = [0,-1,0,1]
board = [[0] * 101 for _ in range(101)]

def findCurve(x,y,d,g) :
    global board
    arr = []
    arr.append(d)
    while True :

        if len(arr) == 2**g:
            break
        for i in range(len(arr)-1,-1,-1) :
            arr.append((arr[i]+1) % 4)
            nx = x + dx[(arr[i]+1) % 4]
            ny = y + dy[(arr[i]+1) % 4]
            if 0 <= nx <= 100 and 0 <= ny <= 100 :
                board[ny][nx] = 1
                x = nx
                y = ny
# def checkRect(x,y) :
#     global answer
#     if 0 <= x+1 < 100 and 0 <= y+1 < 100:
#         if board[x+1][y] == 1 and board[x][y+1] == 1 and board[x+1][y+1] == 1 :
#             answer += 1
#
#             return
#         else :
#             return
#     else :
#         return

answer = 0
for n in range(N) :
    x,y,d,g = map(int,sys.stdin.readline().split())
    board[y][x] = 1
    x = x + dx[d]
    y = y + dy[d]
    board[y][x] = 1
    findCurve(x,y,d,g)
for i in range(100) :
    for j in range(100) :
        if board[i][j] == 1 and board[i][j + 1] == 1 and board[i + 1][j] == 1 and board[i + 1][j + 1] == 1 :
            answer += 1
            # checkRect(i,j)

print(answer)