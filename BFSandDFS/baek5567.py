import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[0] * (n+1) for i in range(n+1)]
visited = [0] * (n+1)
for i in range(1,m+1) :
    a, b = map(int,sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1
answer = []
def bfs(node) :
    global cnt
    que = []
    que.append(node)
    visited[node] = 1
    while que :
        cur = que.pop(0)
        if visited[cur] > 3 :
            break
        answer.append(cur)
        for i in range(1, n+1) :
            if graph[cur][i] == 1 and visited[i] == 0 :
                visited[i] = visited[cur] + 1
                que.append(i)

bfs(1)
print(len(answer)-1)