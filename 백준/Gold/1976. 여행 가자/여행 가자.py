import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

# 도시 연결 여부
city = [list(map(int, input().split())) for _ in range(N)]
# union-find 위한 parent 배열
parents = list(range(N))
# 계획들
plans = list(map(int,sys.stdin.readline().split()))

def find(x) :
    if parents[x] != x :
        parents[x] = find(parents[x])
    return parents[x]

def union(x,y) :
    x = find(x)
    y = find(y)
    if x > y :
        parents[x] = y
    else :
        parents[y] = x

# 연결되있는 도시 union
for i in range(N) :
    for j in range(N) :
        if city[i][j] == 1 :
            union(i,j)
answer= "YES"
# 같은 parent 아니면 NO 출력
for i in range(M) :
    if parents[plans[i]-1] != parents[plans[0] -1] :
        answer = "NO"
        break
print(answer)