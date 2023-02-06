N = int(input())
board = [0]*N
cnt =0 
def promising(x) : # 수직 체크, 대각선 체크 <= 현재 행,열 위치에서 pruning
    for i in range(x):
        if board[x] == board[i] or x-i == abs(board[x]-board[i]):
            return False
    return True
def dfs(x) :
    global cnt
    if x == N :
        cnt += 1
        return
    else :
        for i in range(N) :
            board[x] = i # (x,i)에 퀸이 위치한다.
            if promising(x) : 
                dfs(x+1) # 다음 행 검사
dfs(0)
print(cnt)