import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
vips = []
for _ in range(m) :
    vips.append(int(sys.stdin.readline()))
dp = [1] * (41)
dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3,41) :
    dp[i] = dp[i-1] + dp[i-2]

answer = 1
if m > 0 :
    pre = 0
    for j in range(m) :
        answer *= dp[vips[j]-pre-1]
        pre = vips[j]
    answer *= dp[n-pre]
else :
    answer = dp[n]
print(answer)