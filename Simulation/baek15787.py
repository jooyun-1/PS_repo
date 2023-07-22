import sys

N, M = map(int, sys.stdin.readline().split())
arr = []
train = [[0] * 20 for _ in range(N)]
cnt = 0
for m in range(M) :
    line = list(map(int,sys.stdin.readline().split()))
    first_flag, last_flag = False, False
    i = line[1]
    if len(line) > 2 :
        x = line[2]
    if line[0] == 1 :
            train[i-1][x-1] = 1

    elif line[0] == 2 :
            train[i-1][x-1] = 0
    elif line[0] == 3:
        for k in range(19,0,-1) :
             train[i-1][k] = train[i-1][k-1]
        train[i-1][0] = 0
    elif line[0] == 4 :
        for k in range(19) :
                train[i-1][k] = train[i-1][k+1]
        train[i-1][19] = 0
for i in range(N):
    if train[i] not in arr:
        arr.append(train[i])
        cnt += 1
print(cnt)