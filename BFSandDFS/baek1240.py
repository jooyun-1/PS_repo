import sys
N, M = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
answer = []

for i in range(N-1) :
    a, b, w = map(int,sys.stdin.readline().split())
    graph[a].append((b,w))
    graph[b].append((a,w))

def bfs(start,end) :
    que = list()
    que.append((start,0))
    visited = [0] * (N+1)
    visited[start] = 1
    while que :
        node, w  = que.pop(0)
        if node == end :
            answer.append(w)
            return w
        for i, d in graph[node] :
            if visited[i] == 0:
                visited[i] = 1
                que.append((i,w+d))

for i in range(M) :
    x, y = map(int, sys.stdin.readline().split())
    bfs(x,y)
    # print(bfs(x,y))

for ans in answer :
    print(ans)

# def dfs(start, end) :
#     global dist
#     if start == end :
#         answer.append(dist)
#         return
#     visited[start] = 1
#     for i in range(1,N+1) :
#         if graph[start][i] > 0 and visited[i] == 0 :
#             dist += graph[start][i]
#             dfs(i,end)