import sys
import heapq

N, E = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for i in range(E) :
    a, b, c = map(int,sys.stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
v1,v2 = map(int,input().split())
INF = sys.maxsize

def dijkstra(start,end) :
    distance = [INF] * (N+1)
    distance[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    while q :
        dist, now = heapq.heappop(q)
        if dist > distance[now] :
            continue
        for node, val in graph[now] :
            cost = distance[now] + val
            if cost < distance[node] :
                distance[node] = cost
                heapq.heappush(q,(cost,node))
    return distance[end]

path1 = dijkstra(1,v1) + dijkstra(v1, v2) + dijkstra(v2,N)
path2 = dijkstra(1,v2) + dijkstra(v2, v1) + dijkstra(v1,N)

print(-1) if path1 >= INF and path2 >= INF else print(min(path1,path2))