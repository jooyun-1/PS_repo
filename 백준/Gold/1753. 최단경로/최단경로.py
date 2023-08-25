import sys
import heapq

V, E = map(int,sys.stdin.readline().split())
start = int(sys.stdin.readline())
adj = [[] for _ in range(V+1)]
dist = [float('inf')] * (V+1)
heap = []
for e in range(E) :
    u, v, w = map(int,sys.stdin.readline().split())
    adj[u].append((w,v))

def dijkstra(start) :
    dist[start] = 0
    heapq.heappush(heap,(0,start))

    while heap :
        now_w, now = heapq.heappop(heap)

        if dist[now] < now_w :
            continue

        for w, next in adj[now] :
            next_w = w + now_w
            if next_w < dist[next] :
                dist[next] = next_w
                heapq.heappush(heap,(next_w, next))
dijkstra(start)

for i in range(1,V+1) :
    if dist[i] == float('inf') :
        print('INF')
    else :
        print(dist[i])