# 회색 : 치즈
# 가장자리엔 치즈 X
import sys
a, b = map(int,sys.stdin.readline().split())
visited = [[0] * b for _ in range(a)]
graph, que = [], []
answer = []
time, cnt = 0, 0
for i in range(a) :
    line = list(map(int,sys.stdin.readline().rstrip().split()))
    graph.append(line)

def bfs() :
    que.append([0,0])
    visited[0][0] = 1
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    cnt = 0
    while que :
        x, y = que.pop(0)
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < a and 0 <= ny < b and visited[nx][ny] == 0:
                if graph[nx][ny] == 0 :
                    visited[nx][ny] = 1
                    que.append([nx,ny])

                elif graph[nx][ny] == 1 :
                    visited[nx][ny] = 1
                    graph[nx][ny] = 0
                    cnt += 1
    answer.append(cnt)
    return cnt

while True :
    time += 1
    visited = [[0] * b for _ in range(a)]
    cnt = bfs()
    if cnt == 0 :
        break
print(time-1)
print(answer[-2])

