def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    Max = 102
    visited = [[0] * Max for _ in range(Max)]
    graph = [[-1]*Max for _ in range(Max)]
    for rec in rectangle :
        x1,y1,x2,y2 = map(lambda x: x*2, rec)
        for i in range(x1,x2+1) :
            for j in range(y1,y2+1) :
                if x1<i<x2 and y1<j<y2 :
                    graph[i][j] = 0
                elif graph[i][j] != 0 :
                    graph[i][j] = 1
    que = list()
    que.append([characterX*2,characterY*2])
    visited[characterX*2][characterY*2] = 1
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while que :
        x,y = que.pop(0)
        if x == itemX *2 and y == itemY * 2 :
            answer = visited[x][y] // 2
            break
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if visited[nx][ny] == 0 and graph[nx][ny] == 1 :
                visited[nx][ny] = visited[x][y] + 1
                que.append([nx,ny])
    return answer