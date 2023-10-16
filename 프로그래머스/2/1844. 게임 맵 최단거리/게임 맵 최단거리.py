dx = [1,-1,0,0]
dy = [0,0,1,-1]


def bfs(x,y,maps,n,m) :
    
    que = []
    que.append([x,y])
    visited = [[0] * m for _ in range(n)]
    visited[x][y] = 1

    while que :
        x, y = que.pop(0)
        if x == n-1 and y == m-1 :

            return visited[x][y]
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m :
                if maps[nx][ny] == 1 and visited[nx][ny] == 0 :
                    visited[nx][ny] = visited[x][y] + 1
                    que.append([nx,ny])
def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[len(maps)-1])
    answer = bfs(0,0,maps,n,m)
    if answer == None :
        answer = -1
    return answer
