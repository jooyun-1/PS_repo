import heapq
def solution(scoville, K):
    answer = 0
    heap = []
    for i in range(len(scoville)) :
        heapq.heappush(heap,scoville[i])
    while True :
        if heap[0] >= K :
            break
        if len(heap) < 2 :
            answer = -1
            break
        firstVal = heapq.heappop(heap)
        secondVal = heapq.heappop(heap)
        temp = firstVal + (secondVal*2)
        heapq.heappush(heap,temp)
        answer += 1
    return answer