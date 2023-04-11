import sys
N = int(sys.stdin.readline())
graph = []
answer = []
visited = [0] * N

for i in range(N) :
    line = list(map(int,sys.stdin.readline().rstrip().split()))
    graph.append(line)

def dfs(node) :
    for i in range(N) :
        if node == i :
            continue
        if graph[node][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i)

for i in range(N) :
    visited = [0] * N
    dfs(i)
    answer.append(visited)
for i in range(len(answer)) :
    for j in range(len(answer[i])):
        print(answer[i][j], end = ' ')
    print()