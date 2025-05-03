import sys

board = []
blank = []

for i in range(9) :
    arr = list(map(int,sys.stdin.readline().split()))
    board.append(arr)

for i in range(9) :
    for j in range(9) :
        if board[i][j] == 0 :
            blank.append((i,j))

def checkrow(x,num) :
    for i in range(9) :
        if num == board[x][i] :
            return False
    return True

def checkcol(y,num) :
    for i in range(9) :
        if num == board[i][y] :
            return False
    return True

def checkrect(x,y,num) :
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if num == board[nx+i][ny+j]:
                return False
    return True
    
def dfs(idx) :
    if idx == len(blank) :
        for i in range(9) :
            print(*board[i])
        exit(0)
    for i in range(1,10) :
        x = blank[idx][0]
        y = blank[idx][1]
        if checkrow(x,i) and checkcol(y,i) and checkrect(x,y,i) :
            board[x][y] = i
            dfs(idx+1)
            board[x][y] = 0
dfs(0)