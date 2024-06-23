import sys

n = int(sys.stdin.readline())
board = []
answer = []
visited = [[0] * n for _ in range(n)]
for i in range(n):
    line = list(map(int, sys.stdin.readline().rstrip()))
    board.append(line)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 1


def dfs(x, y, p):
    global cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] == 1 and visited[nx][ny] == 0:
                cnt += 1
                visited[nx][ny] = 1
                dfs(nx, ny, p + 1)
    return cnt


for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
            cnt = dfs(i, j, 0)
            answer.append(cnt)
            cnt = 1
answer.sort()
print(len(answer))
for ans in answer:
    print(ans)

