# def bfs() :
from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(x,y,places) :
    que = deque()
    visited = [[0] * 5 for _ in range(5)]
    distance = [[0] * 5 for _ in range(5)]
    start_x, start_y = x, y
    visited[x][y] = 1
    que.append((x,y))
    while que :
        cx, cy = que.popleft()
        # print('c',cx,cy)
        # print(places[cx][cy])
        for i in range(4) :
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5 :
                if places[nx][ny] == 'O' and visited[nx][ny] == 0 :
                    que.append((nx,ny))
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[cx][cy] + 1
                elif places[nx][ny] == 'P' and visited[nx][ny] == 0:
                    # print(places,nx,cx,ny,cy,distance[cx][cy])
                    if distance[cx][cy] <= 1 :
                        return 0
    return 1
def solution(places):
    answer = []


    for p in places :
        flag = True
        for i in range(5) :
            if flag == False :
                break
            for j in range(5) :
                if p[i][j] == 'P' :
                    res = bfs(i,j,p)
                    if res == 0 :
                        answer.append(0)
                        flag = False
                        break
        if flag :
            answer.append(1)
    
    return answer