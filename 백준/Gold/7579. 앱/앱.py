N, M = map(int, input().split())

memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

dp = [[0] * (sum(cost)+1) for _ in range(N + 1)]

result = float('inf')
# dp[i][j] => 1~i번째 앱까지, j의 cost로 확보 가능한 메모리의 최대
for i in range(1, N + 1):
    for j in range(sum(cost) + 1):
        if j >= cost[i - 1]: # 메모리 확보 가능할 때
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost[i - 1]] + memory[i - 1])
        else:
            dp[i][j] = dp[i - 1][j]

        # 현재 dp[i][j]의 값이 필요한 메모리 M 이상이 된다면
        if (dp[i][j] >= M):
            # 해당 j cost와 이전 j cost를 비교해, 더 작은 cost 값을 사용
            result = min(result, j)

print(result)