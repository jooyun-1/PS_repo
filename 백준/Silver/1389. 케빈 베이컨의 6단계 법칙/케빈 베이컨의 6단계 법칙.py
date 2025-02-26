import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
for i in range(M) :
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start, end) :
    que = deque([])
    que.append(start)
    visited = [-1] * (N+1)
    visited[start] = 0
    while que :
        node = que.popleft()
        if node == end :
            return visited[node]
        for n in graph[node] :
            if visited[n] == -1 :
                visited[n] = visited[node] + 1
                que.append(n)

answer = [0] * (N+1)
for i in range(1,N+1) :
    for j in range(1,N+1) :
        if i == j :
            continue
        else :
            cnt = bfs(i,j)
            answer[i] += cnt

answer.pop(0)
min_val = min(answer)
for i in range(len(answer)) :
    if answer[i] == min_val :
        print(i+1)
        break
