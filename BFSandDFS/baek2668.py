import sys
N = int(sys.stdin.readline())
# graph = [[0] * (N+1) for i in range(N+1)]
graph = [[] * (N+1) for i in range(N+1)]
visited = [0] * (N+1)
finished = [0] * (N+1)
answer = []
for i in range(1,N+1) :
    j = int(sys.stdin.readline())
    graph[j].append(i)

def dfs(node,i) :    
    visited[node] = 1 
    for a in graph[node] :                  
        if visited[a] == 0 :
            dfs(a,i)
        elif a == i and visited[a] == 1 :
            answer.append(a)

answer = []  
for i in range(1, N+1) :
    visited = [0] * (N+1)
    dfs(i,i)
print(len(answer))
for ans in answer :
    print(ans)

