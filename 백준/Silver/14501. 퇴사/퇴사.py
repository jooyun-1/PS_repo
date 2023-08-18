# N일동안 최대한 많은 상담, N+1째 되는 날 퇴사
# 하루에 하나씩 서로 다른 사람 상담
# T : 기간, P : 금액
# 최대 수익

N = int(input())
arr = []
dp = [0] * (N+1)
for n in range(N) :
    T, P = map(int,input().split())
    arr.append([T,P])
for i in range(N) :
    for j in range(i + arr[i][0], N+1) :
        if dp[j] < dp[i] + arr[i][1] :
            dp[j] = dp[i] + arr[i][1]
print(dp[-1])