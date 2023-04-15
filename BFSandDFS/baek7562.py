import sys
t = int(sys.stdin.readline())
answer = []

dx = [2,-2,2,-2,1,-1,1,-1]
dy = [1,-1,-1,1,2,-2,-2,2]

def bfs(x,y, ans_x, ans_y) :
    que = []
    global visited
    que.append([x,y])

    while que :
        x, y = que.pop(0)

        if x == ans_x and y == ans_y :
            answer.append(visited[x][y])
            break
        else :
            for i in range(8) :
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= 0 and nx < length and ny >=0 and ny < length :
                    if visited[nx][ny] == 0 :
                        visited[nx][ny] = visited[x][y] + 1
                        que.append([nx,ny])

for i in range(t) :
    length = int(sys.stdin.readline())
    visited = [[0] * length for _ in range(length)]
    x, y = map(int,sys.stdin.readline().split())
    ans_x, ans_y = map(int,sys.stdin.readline().split())
    bfs(x,y,ans_x,ans_y)
for ans in answer :
    print(ans)
