# N x M, 새로 새울 수 있는 벽 = 3개
# 0 = 빈칸, 1 = 벽, 2 = 바이러스
# 안전 영역의 최대 크기
import sys
import copy
n, m = map(int, sys.stdin.readline().split())
graph = []
for i in range(n) :
    line = list(map(int,sys.stdin.readline().rstrip().split()))
    graph.append(line)
dx = [-1,0,1,0]
dy = [0,-1,0,1]
result = 0

def bfs():
    queue = list()
    #queue에 2의 위치 전부 append
    temp = copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                queue.append([i,j])

    while queue:
        x,y = queue.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0<=nx<n) and (0<=ny<m):
                if temp[nx][ny] == 0:
                    temp[nx][ny] =2
                    queue.append([nx,ny])

    global result
    count = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                count +=1

    result = max(result, count)


def make_wall(count):
    if count == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_wall(count+1)
                graph[i][j] = 0

make_wall(0)

print(result)