import sys
N = int(sys.stdin.readline())
arr =list()
size = list()
rank = 1
for i in range(N) :
    x, y = map(int, sys.stdin.readline().split())
    arr.append([x,y])

for i in range(N) :
    for j in range(N) :
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1] :
            rank += 1
    size.append(rank)
    rank = 1

for s in size :
    print(s, end= " ")