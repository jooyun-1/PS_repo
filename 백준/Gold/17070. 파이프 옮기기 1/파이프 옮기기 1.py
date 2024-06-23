import sys

N = int(sys.stdin.readline())
house = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [1, 0, 1]  # 아래, 오른쪽, 오른 대각선
dy = [0, 1, 1]
cnt = 0


def dfs(x, y, dir):
    global cnt
    if house[x][y] == 1:
        return
    if x == N - 1 and y == N - 1:
        cnt += 1
        return
    if x + 1 < N and y + 1 < N :
        if house[x+1][y+1] == 0 and house[x+1][y] == 0 and house[x][y+1] == 0 :
            dfs(x+1,y+1,2)
    if dir == 0 or dir == 2 :
        if y + 1 < N :
            if house[x][y+1] == 0 :
                dfs(x,y+1,0)
    if dir == 1 or dir == 2 :
        if x + 1 < N :
            if house[x+1][y] == 0 :
                dfs(x+1,y,1)

dfs(0, 1, 0)
print(cnt)