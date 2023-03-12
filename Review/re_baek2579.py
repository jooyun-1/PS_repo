# 한 번에 한 계단씩, 두 계단씩
# 연속된 세 개의 계단 밟으면 X
# 마지막 계단은 반드시 밟아야 한다.
import sys
N = int(sys.stdin.readline())
stairs = [0]
for i in range(1, N+1) :
    stairs.append(int(sys.stdin.readline()))
DP = [0] * (N+1)
if N == 1 :
    print(stairs[1])
elif N == 2 :
    print(stairs[1] + stairs[2])
else :
    DP[1] = stairs[1]
    DP[2] = DP[1] +stairs[2]

    for i in range(3,N+1) :
        DP[i] = max(DP[i-2]+stairs[i], DP[i-3]+stairs[i-1] + stairs[i])
    print(DP[N])

