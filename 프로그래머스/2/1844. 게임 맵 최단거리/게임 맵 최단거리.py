from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for _ in range(n)]
    deq = deque()
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    def bfs(x, y) :
        visited[x-1][y-1] = 1
        deq.append((x-1,y-1))
        flag = False
        cnt = 1
        while deq :
            cx, cy = deq.popleft()
            if cx == n -1 and cy == m - 1 :
                flag = True
                return visited[cx][cy]
            for i in range(4) :
                nx = cx + dx[i]
                ny = cy + dy[i]
                if 0 <= nx < n and 0 <= ny < m :
                    if maps[nx][ny] == 1 and visited[nx][ny] == 0 :
                        deq.append((nx,ny))
                        visited[nx][ny] = visited[cx][cy] + 1
                        cnt += 1
        if flag == False :
            return -1
        
    answer = bfs(1,1)
    return answer