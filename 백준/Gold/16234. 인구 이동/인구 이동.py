import sys
sys.setrecursionlimit(1000000)
N, L, R = map(int,sys.stdin.readline().split())
land = []
for n in range(N) :
    line = list(map(int,sys.stdin.readline().split()))
    land.append(line)
dir = [[1,0],[0,1],[-1,0],[0,-1]]

def move(x,y) :
    global arr,sum,cnt,flag
    for i,j in dir :
        nx = x + i
        ny = y + j
        if 0 <= nx < N and 0 <= ny < N :
            if visited[nx][ny] == 0 and L <= abs(land[nx][ny] - land[x][y]) <= R :
                # print(nx, ny, land[nx][ny])
                visited[nx][ny] = 1
                sum += land[nx][ny]
                cnt += 1
                # if [nx,ny] not in arr :
                arr.append([nx,ny])
                move(nx,ny)
answer = 0
while True :
    visited = [[0] * (N) for i in range(N)]
    flag = False
    # print(land)
    for i in range(N) :
        for j in range(N) :
            if visited[i][j] == 0 :
                cnt,sum = 1, land[i][j]
                arr = [[i,j]]
                visited[i][j] = 1
                move(i,j)
                num = sum // cnt
                # print(num,sum,cnt)
                if len(arr) > 1 :
                    flag = True
                    for a in range(len(arr)) :
                        land[arr[a][0]][arr[a][1]] = num
    if flag == True :
        answer += 1
        # print(answer)
    if flag == False :
        break

print(answer)