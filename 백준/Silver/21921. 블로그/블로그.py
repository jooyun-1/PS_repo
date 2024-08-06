import sys

N, X = map(int,sys.stdin.readline().split())
visited = list(map(int,sys.stdin.readline().split()))

if max(visited) == 0 :
    print('SAD')
    exit(0)
    
val = sum(visited[:X])
max_val = val
max_cnt = 1

for i in range(X,N) :
    val += visited[i]
    val -= visited[i-X]
    if val > max_val :
        max_val = val
        max_cnt = 1
    elif val == max_val :
        max_cnt += 1
print(max_val)
print(max_cnt)