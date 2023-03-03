# 1부터 모든 자연수를 오름차순으로 노래
# K를 노래할 때 K마리의 새가 날아감
# 현재 나무의 새 < K  : 1부터 게임 다시 시작
# 노래 하나 1초
import sys
N = int(sys.stdin.readline())
cnt, K = 0, 1

while N > 0 :     
    if N < K :
        K = 1
    N -= K
    K += 1
    cnt += 1
print(cnt)
