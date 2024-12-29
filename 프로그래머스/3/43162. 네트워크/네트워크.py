def solution(n, computers):
    answer = 0
    visited = [0] * n

    def dfs(node) :
        visited[node] = 1
        for x in range(n) :
            if x != node and computers[node][x] == 1 :
                if visited[x] == 0 :
                    visited[x] = 1
                    dfs(x)
                
    for com in range(n) :
        if visited[com] == 0 :
            dfs(com)
            answer += 1
    return answer