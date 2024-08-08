import sys
import heapq

n = int(sys.stdin.readline())
heap = []
answer = []
for i in range(n) :
    num = int(sys.stdin.readline())
    if num == 0 :
        if len(heap) == 0 :
            answer.append(0)
        else :
            answer.append(heapq.heappop(heap))
    else :
        heapq.heappush(heap,num)
        
for ans in answer :
    print(ans)