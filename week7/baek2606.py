n = int(input())
m = int(input())
graph = [[0] * (n+1) for i in range(n+1)]
visited = [0] * (n+1)
virus_cnt = 0

for i in range(m) :
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

def dfs(start) :
    global virus_cnt
    visited[start] = 1
    for i in range(n+1) :
        if graph[start][i] == 1 and visited[i] == 0 :
            virus_cnt += 1
            dfs(i)
    return virus_cnt
dfs(1)
print(virus_cnt)
