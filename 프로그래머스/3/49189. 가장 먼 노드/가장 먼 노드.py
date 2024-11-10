from collections import deque
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    distance = [-1] * (n+1)
    
    for ed in edge :
        graph[ed[0]].append(ed[1])
        graph[ed[1]].append(ed[0])
    deq = deque([1])
    distance[1] = 0
    while deq :
        now = deq.popleft()
        for i in graph[now] :
            if distance[i] == -1 :
                deq.append(i)
                distance[i] = distance[now] + 1
    for d in distance :
        if d == max(distance) :
            answer += 1
            
    return answer