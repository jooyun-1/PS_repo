import sys
from itertools import combinations

N = int(sys.stdin.readline())

area = [i for i in range(1,N+1)]
human_num = dict()
num = list(map(int,sys.stdin.readline().rstrip().split()))
for i in range(1,N+1) :
    human_num[i] = num[i-1]

node = dict()
visited = [0] * (N+1)
for i in range(1,N+1) :
    line = list(map(int,sys.stdin.readline().rstrip().split()))
    temp = []
    for j in range(line[0]) :
        temp.append(line[j+1])
    node[i] = temp
minVal = float('inf')

def dfs(x,arr) :
    global flag
    visited[x] = 1
    # print(x,arr,visited)
    if visited.count(1) == len(arr) :
        # print(x, arr, visited)
        flag = True
        return
    else :
        for n in node[x] :
            if n in arr and visited[n] == 0:
                visited[n] = 1
                dfs(n,arr)

for n in range(1,N+1) :
    com = list(combinations(area,n))
    for c in com :
        one, two = [], []
        for i in c :
            one.append(i)
        for a in area :
            if a not in one :
                two.append(a)
        visited = [0] * (N+1)
        flag = False
        dfs(one[0], one)
        if flag == True :
            visited = [0] * (N + 1)
            flag = False
            if len(two) > 0 :
                dfs(two[0], two)

        if flag == True :
            cnt1, cnt2 = 0, 0
            for o in one:
                cnt1 += human_num[o]
            for t in two:
                cnt2 += human_num[t]
            minVal = min(minVal, (abs(cnt1 - cnt2)))
if minVal == float('inf') :
    print(-1)
else :
    print(minVal)