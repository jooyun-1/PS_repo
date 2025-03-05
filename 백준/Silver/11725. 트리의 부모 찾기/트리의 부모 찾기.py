import sys
sys.setrecursionlimit(10**6)
 
N = int(sys.stdin.readline())
 
# 그래프 생성
graph = [[] for i in range(N+1)]
for i in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
 
# 방문 여부, 각 인덱스를 노드로 사용해 방문했으면 0을 지우고, 부모 노드를 저장한다.
visited = [0]*(N+1) 

def dfs(node) :
    for i in graph[node] :
        if visited[i] == 0 :
            visited[i] = node
            dfs(i)
dfs(1)

for x in range(2, N+1):
    print(visited[x]) # 각 인덱스(노드)에 저장된 부모 노드 가져오기