import sys 
sys.setrecursionlimit(10000)

dx = [1,-1,0,0]
dy = [0,0,1,-1]
answer = []
cnt = 0

def dfs(x,y,maps,rows,cols,visited) :
    global cnt
    
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < rows and 0 <= ny < cols :
            if maps[nx][ny] != 'X' and visited[nx][ny] == 0 :
                visited[nx][ny] = 1
                # visited[nx][ny] = 1
                cnt += int(maps[nx][ny])
                dfs(nx,ny,maps,rows,cols,visited)
    
def solution(maps):
    global cnt
    rows = len(maps)
    cols = len(maps[0])
    visited = [[0] * cols for _ in range(rows)]
    for i in range(len(maps)) :
        for j in range(len(maps[i])) :
            if maps[i][j] != 'X' and visited[i][j] == 0:
                cnt = int(maps[i][j])
                visited[i][j] = 1
                dfs(i,j,maps,rows,cols,visited)
                answer.append(cnt)
    if len(answer) > 0 :
        answer.sort()
    else :
        answer.append(-1)
    return answer