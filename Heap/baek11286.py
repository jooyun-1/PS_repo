# 절댓값 힙
# 1. 배열에 정수 x를 넣는다 (x is not 0)
# 2. 배열에서 절댓값이 가장 작은 값 출력하고 그 값 배열에서 제거(pop)
#    여러 개일 때는, 가장 작은 수를 출력하고 그 값을 배열에서 제거
# x= 0 => pop

import sys
import heapq

N = int(sys.stdin.readline())
heap, answer = [], []
for i in range(N) :
    num = int(sys.stdin.readline())
    if num != 0 :
        heapq.heappush(heap,(abs(num),num))
    if len(heap) > 0 :
        if num == 0 :
            answer.append(heapq.heappop(heap)[1])
    elif len(heap) == 0:
        answer.append(0)
for ans in answer :
    print(ans)
