# N : 정점의 개수, M : 간선의 개수, V : 시작 정점 번호
import sys

N, M, V = map(int,sys.stdin.readline().split())
# graph = [[0] * (N+1) for i in range(N+1)]
graph = dict()
for i in range(M) :
    a, b = map(int,sys.stdin.readline().split())
   # graph[a][b] = graph[b][a] = 1
    if a not in graph.keys() or b not in graph.keys():
        graph[a] = [b]
        graph[b] = [a]
    else : 
        graph[a].append(b)
        graph[b].append(a)
print(graph)
# BFS (dict, que 이용)
def bfs(graph,start) :
    visited, need_visit = list(), list()
    need_visit.append(start)
    while need_visit :
        node = need_visit.pop(0)
        if node not in visited :
            visited.append(node)
            if node in graph.keys() :
                print(node)
                need_visit.extend(graph[node])   
    return visited

# DFS (dict, stack 이용)
def dfs(graph, start) :
    need_visit, visited = list(), list()
    need_visit.append(start)
    while need_visit :
        node = need_visit.pop()
        if node not in visited :
            visited.append(node)
            if node in graph.keys() :
                temp = sorted(graph[node],reverse=True)
                need_visit.extend(temp)
    return visited
print(dfs(graph, V))
print(bfs(graph, V))