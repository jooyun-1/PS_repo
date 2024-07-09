def solution(n, computers):
    answer = 0
    visited = [0] * n
    for i in range(n):
        if visited[i] == 0:
            dfs(n, computers, i, visited)
            answer += 1 #DFS로 최대한 컴퓨터들을 방문하고 빠져나오게 되면 그것이 하나의 네트워크.
    return answer

def dfs(n, computers, x, visited):
    visited[x] = 1
    for i in range(n):
        if i != x and computers[x][i] == 1: #연결된 컴퓨터
            if visited[i] == 0:
                dfs(n, computers, i, visited)