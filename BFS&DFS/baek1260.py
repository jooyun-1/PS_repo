import sys

N, M, V = map(int,sys.stdin.readline().split()) 
graph = [[0] * (N+1) for i in range(N+1)] # graph 0으로 모두 초기화
visited = [0] * (N+1) # 방문한 노드 배열 

for i in range(M) :
    a, b = map(int,sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1 # 이어진 곳은 1로 설정

# DFS (recursion)
def dfs(V) :
    visited[V] = 1  # 방문한 노드 1로 설정
    print(V, end=' ')  
    for i in range(1, N+1) :
        if visited[i] == 0 and graph[V][i] == 1 :   
            dfs(i) 
# BFS
def bfs(V) :
    need_visit = list()
    need_visit.append(V) # 앞으로 방문해야되는 곳 queue에 입력
    visited[V] = 0  # dfs함수에서 1로 설정되어있으므로 거꾸로 방문한 곳 0으로 설정
    while need_visit :  # 큐가 빌 때까지
        V = need_visit.pop(0)   # 맨 앞의 노드부터 방문
        print(V, end = ' ')
        for i in range(1, N+1) :
            if visited[i] == 1 and graph[V][i] == 1 :
                visited[i] = 0
                need_visit.append(i)
dfs(V)
print()                
bfs(V)

# DFS
# def dfs(V) :
#    visited[V] = 1
#    need_visit = list()
#    need_visit.append(V)
#    while need_visit :
#        V = need_visit.pop()
#        print(V, end=' ')
#        for i in range(1, N+1):
#            if visited[i] == 0 and graph[V][i] == 1 :
#                need_visit.append(i)
#                visited[i] = 1 
