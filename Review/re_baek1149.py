# 1번 집의 색 != 2번 집의 색
# N번 집의 색 != (N-1)번 집의 색
# i번 집의 색 != i+1,i-1 번 집의 색
import sys

N = int(sys.stdin.readline())
DP = [[] * (N) for i in range(N)]
for i in range(N) :
    DP[i] = list(map(int,sys.stdin.readline().split()))

for i in range(1,N) :
    DP[i][0] = min(DP[i-1][1], DP[i-1][2]) + DP[i][0]
    DP[i][1] = min(DP[i-1][0], DP[i-1][2]) + DP[i][1]
    DP[i][2] = min(DP[i-1][0], DP[i-1][1]) + DP[i][2]
    
print(min(DP[N-1]))