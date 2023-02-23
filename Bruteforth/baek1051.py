import sys

N, M = map(int, input().split())

graph = []
max_size = 1
check = min(N,M)

for i in range(N) :
    s = sys.stdin.readline()
    graph.append(s)

for i in range(N) :
    for j in range(M) :
        for k in range(check) :
            if j+k < M and i+k <N and graph[i][j] == graph[i][j+k] == graph[i+k][j]==graph[i+k][j+k] :
                max_size = max(max_size, (k+1)*(k+1))
print(max_size)
