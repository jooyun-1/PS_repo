# 1번의 해킹 => 여러 개의 컴퓨터 해킹
# 신뢰, 신뢰 X 관계
# A -> B 신뢰하는 경우, B를 해킹하면 A도 해킹 가능
# 한번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호
import sys
from collections import deque
N, M = map(int,sys.stdin.readline().split())
graph = [[] * (N+1) for i in range(N+1)]
answer = [0]
# que = []
for i in range(M) :
    a, b = map(int,sys.stdin.readline().split())
    # graph[b][a] = 1
    graph[b].append(a)
def bfs(node) :
    cnt = 1
    # que.append(node)
    que = deque([node])
    visited = [0] * (N+1)
    visited[node] = 1
    while que :
        node = que.popleft()      
        cnt += 1
#        for n in range(1,N+1) :
        for n in graph[node] :
            if visited[n] == 0 :
                 que.append(n)
                 visited[n] = 1           
    # answer.append(cnt)
    return cnt
max_cnt = 1
for i in range(1,N+1) :   
    cnt = bfs(i)
    if cnt > max_cnt :
        max_cnt = cnt
        answer = []
        answer.append(i)
    elif cnt == max_cnt :
        answer.append(i)      
for ans in answer :
        print(ans, end = " ")


# dfs 메모리 초과
# def dfs(node) :
#     global cnt
#     visited[node] = 1
#     cnt += 1
#     for i in range(1,N+1) :
#         if graph[node][i] == 1 and visited[i] == 0 :
#             dfs(i)
