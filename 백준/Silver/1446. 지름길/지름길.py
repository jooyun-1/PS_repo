import sys
import heapq

INF = sys.maxsize

def dijkstra(start) :
    que = []
    heapq.heappush(que, (0, start))
    distance[start] = 0
    while que :
        dist, now = heapq.heappop(que)
        if dist > distance[now] :
            continue
        for i in graph[now] :
            cost = dist + i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(que,(cost,i[0]))

n, d = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(d+1)]
distance = [INF] * (d+1)

for i in range(d) :
    graph[i].append((i+1,1))

for _ in range(n) :
    start, end, l = map(int, sys.stdin.readline().split())
    if end > d :
        continue
    else :
        graph[start].append((end,l))

dijkstra(0)
print(distance[d])