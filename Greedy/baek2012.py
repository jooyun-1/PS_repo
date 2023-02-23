# N명 참가, 예상등수 적음
# 불만도 abs(A-B) A:예상, B: 실제
# 불만도 합 최소!
import sys
N = int(sys.stdin.readline())
rank = []
sum = 0
for i in range(1, N+1) :
    rank.append(int(sys.stdin.readline()))
rank.sort()
for j in range(1, N+1) :
    sum += abs(j - rank[j-1])
print(sum)
