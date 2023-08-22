import sys
from collections import deque
N = int(sys.stdin.readline())
space = []
fish = []
dx = [-1,0,0,1]
dy = [0,-1,1,0]
for n in range(N) :
    line = list(map(int,sys.stdin.readline().rstrip().split()))
    space.append(line)
    for l in range(len(line)) :
        if space[n][l] == 9 :
            space[n][l] = 0
            curX, curY = n, l
curSize = 2
answer = 0
def bfs(x, y) :
    global curSize
    visited = [[0] * N for _ in range(N)]
    distance = [[0] * N for _ in range(N)]
    que = deque()
    que.append([x,y])
    arr = []
    while que :
        x, y = que.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N :
                if space[nx][ny] <= curSize and visited[nx][ny] == 0 :
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[x][y] + 1
                    que.append([nx, ny])

                    if space[nx][ny] != 0 and space[nx][ny] < curSize:
                        arr.append([nx,ny,distance[nx][ny]])
    arr.sort(key = lambda x : (x[2],x[0],x[1]))
    return arr
cnt = 0
while True :
    fishList = bfs(curX, curY)
    if len(fishList) == 0 :
        print(answer)
        exit(0)
    curX, curY, dist = fishList[0]
    cnt += 1  # 잡아먹은 물고기 횟수 증가
    if cnt == curSize:  # size만큼 잡아먹었을 때
        curSize += 1  # 크기 증가
        cnt = 0  # cnt를 0 초기화
    answer += dist
    space[curX][curY] = 0  # 잡아먹었으므로 0으로 채움