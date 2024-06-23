import sys
import heapq

N, M, X = map(int,sys.stdin.readline().split())
village = [[] for _ in range(N+1)]
INF = float('inf')

def dijkstra(start) :
    arr = []
    distance = [INF] * (N+1)
    heapq.heappush(arr,(0,start))
    distance[start] = 0 # 출발 노드의 distance 값을 0으로 설정

    while arr :
        dist, now = heapq.heappop(arr) # distance[now], 현재 노드
        for index, next_cost in village[now] :
            cost = dist + next_cost

            if distance[index] > cost :
                distance[index] = cost
                heapq.heappush(arr,(cost,index))
    return distance

for m in range(M) :
    a, b, t = map(int,sys.stdin.readline().split())
    village[a].append((b,t))

answer = 0
for i in range(1,N+1) :
    first = dijkstra(i)
    second = dijkstra(X)
    answer = max(answer, first[X] + second[i])

print(answer)