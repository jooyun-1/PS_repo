from collections import deque

def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n+1)]

    for i in range(len(wires)) :
        a, b = wires[i][0], wires[i][1]
        graph[a].append(b)
        graph[b].append(a)
    
    def bfs(node) :
        que = deque()
        que.append(node)
        visited = [0] * (n+1)
        visited[node] = 1
        cnt = 0
        while que :
            x = que.popleft()
            for i in graph[x] :
                if visited[i] == 0 :
                    visited[i] = 1
                    que.append(i)
                    cnt += 1
        return cnt
    
    for i in range(len(wires)) :
        a, b = wires[i][0], wires[i][1]
        
        graph[a].remove(b)
        graph[b].remove(a)
        
        answer = min(answer,abs(bfs(a) - bfs(b)))
        
        
        graph[a].append(b)
        graph[b].append(a)
        
    return answer