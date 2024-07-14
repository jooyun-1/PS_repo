from collections import deque

def solution(n, edge):
    answer = 0
    graph =[[] for _ in range(n+1)]
    visited = [-1] * (n+1)
    for e in edge :
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    
    deq = deque()
    def bfs(node) :
        deq.append(node)
        visited[1] = 0
        while deq :
            x = deq.popleft()
            for i in graph[x] :
                if visited[i] == -1 :
                    visited[i] = visited[x] + 1
                    deq.append(i)
    bfs(1)
    for v in visited :
        if v == max(visited) :
            answer += 1
    return answer