import sys

n, k = map(int,sys.stdin.readline().split())
coins = []

for i in range(n) :
    coins.append(int(sys.stdin.readline()))

dp = [0 for _ in range(k+1)]
dp[0] = 1
for c in coins :
    for i in range(k+1) :
        if i - c >= 0 :
            dp[i] += dp[i-c]
print(dp[k])
