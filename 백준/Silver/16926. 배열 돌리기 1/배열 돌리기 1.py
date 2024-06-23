import sys

N, M, R = map(int, sys.stdin.readline().split())
arr = []
for i in range(N) :
    line = list(map(int,sys.stdin.readline().split()))
    arr.append(line)

dx = [0,1,0,-1]
dy = [1,0,-1,0]
num = min(N,M) // 2
def dfs() :
    for i in range(num) :
        temp = arr[i][i]
        cnt = 0
        x, y = i, i

        while cnt < 4 :
            nx = x + dx[cnt]
            ny = y + dy[cnt]
            if nx >= i and ny >= i and nx < N - i and ny < M - i :
                arr[x][y] = arr[nx][ny]
                x = nx
                y = ny

            else :
                cnt += 1
        arr[i+1][i] = temp

for r in range(R) :
    dfs()

for i in range(N) :
    for j in range(M) :
        print(arr[i][j], end = ' ')
    print()