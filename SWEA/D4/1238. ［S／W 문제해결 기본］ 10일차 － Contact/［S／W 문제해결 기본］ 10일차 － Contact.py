
from collections import defaultdict

def bfs(x) :
    que = []
    que.append(x)
    while que :
        x = que.pop(0)
        # print(x,visited[x])
        for nx in contact[x] :
            if visited[nx] == 0 :
                visited[nx] = visited[x] + 1
                que.append(nx)

for t in range(1,11) :
    n, start = map(int, input().split())

    line = list(map(int,input().rstrip().split()))
    contact = defaultdict(list)
    humans = set()
    for i in range(len(line) // 2) :
        contact[line[i*2]].append(line[i*2+1])
        contact[line[i * 2]].sort()

    visited = [0] * (101)

    bfs(start)
    maxVal = max(visited)
    for i in range(len(visited)) :
        if visited[i] == maxVal :
            answer = i

    print("#{} {}".format(t,answer))