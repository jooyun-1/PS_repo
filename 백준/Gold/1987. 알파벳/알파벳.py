# 지금까지 지나온 모든 칸에 적혀있는 알파벳과 달라야 한다.
# 말이 최대 몇 칸을 지날 수 있는지?
import sys
R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
words = set()
dx = [1,-1,0,0]
dy = [0,0,1,-1]

answer = 0
def dfs(x, y,cnt) :
    global answer
    answer = max(answer, cnt)
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and board[nx][ny] not in words :
                words.add(board[nx][ny])
                dfs(nx,ny,cnt+1)
                words.remove(board[nx][ny])
words.add(board[0][0])
dfs(0,0,1)
print(answer)

