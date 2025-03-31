import sys

n = int(input())

dp = [0] * (n+1)
dp[1] = 1

for i in range(2,n+1) :
    minVal = sys.maxsize
    for j in range(1,int(i**0.5)+1) :
        minVal = min(minVal, dp[i-(j**2)])
    dp[i] = minVal + 1
print(dp[n])