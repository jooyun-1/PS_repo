import sys

T = int(sys.stdin.readline())
for t in range(T):
    N, M = map(int, sys.stdin.readline().split())
    arr = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

    answer = 0
    temp = []
    # +형
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # x형
    dx2 = [1, -1, -1, 1]
    dy2 = [1, 1, -1, -1]

    # +형
    for x in range(N):
        for y in range(N):
            sum = arr[x][y]
            for m in range(1,M):
                for k in range(4):
                    nx = x+dx[k]*m
                    ny = y+dy[k]*m
                    if 0<=nx<N and 0<=ny<N:
                        sum += arr[nx][ny]
            temp.append(sum)

    # x형
    for x in range(N):
        for y in range(N):
            sum = arr[x][y]
            for m in range(1,M):
                for k in range(4):
                    nx = x+dx2[k]*m
                    ny = y+dy2[k]*m
                    if 0<=nx<N and 0<=ny<N:
                        sum += arr[nx][ny]
            temp.append(sum)
    print('#{} {}'.format(t+1,max(temp)))
