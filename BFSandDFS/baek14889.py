import sys
N = int(sys.stdin.readline())
S = []
visited = [0] * N
sum, sum2 = 0, 0
answer = float('inf')

for i in range(N) :
    line = list(map(int, sys.stdin.readline().rstrip().split()))
    S.append(line)

def dfs(depth,index) :
    global answer
    if depth == N//2:
        sum, sum2 = 0, 0
        for i in range(N) :
            for j in range(N) :
                if visited[i] == 1 and visited[j] == 1:
                    sum += S[i][j]
                elif visited[i] == 0 and visited[j] == 0:
                    sum2 += S[i][j]
        answer = min(answer, abs(sum-sum2))

    for i in range(index,N) :
        if visited[i] == 0 :
            visited[i] = 1
            dfs(depth+1,i+1)
            visited[i] = 0

dfs(0,0)
print(answer)