from collections import deque
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    for v in edge :
        graph[v[0]].append(v[1])
        graph[v[1]].append(v[0])
    visited = [0] * (n+1)
    def bfs(node) :        
        deq = deque([])
        visited[node] = 1
        deq.append(node)
        while deq :
            # print(deq)
            x = deq.popleft()
            for n in graph[x] :
                if visited[n] == 0 :
                    deq.append(n)
                    visited[n] = visited[x] + 1
    bfs(1)
    max_val = max(visited)
    print(visited)
    for v in visited :
        if v == max_val :
            answer += 1
    return answer