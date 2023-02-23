# 배열에 자연수 x를 넣는다.
# 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.
# N= 연산의 개수, x=0 => 가장 큰 값을 출력하고 그 값을 배열에서 제거
import heapq
import sys

heap = []
N = int(input())
for i in range(N) :
    i = int(sys.stdin.readline())
    if i == 0:
        if len(heap) == 0 :
            print(0)
        else:
           print(-heapq.heappop(heap))
    else :
        heapq.heappush(heap,-i) 
        

