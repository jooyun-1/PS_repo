import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while True :
        if len(scoville) >= 2 :
            first = heapq.heappop(scoville)
            if first >= K :
                break
            second = heapq.heappop(scoville)
            new = first + (second * 2)
            heapq.heappush(scoville,new)
            answer += 1
        # elif len(scoville) == 2 :
        #     first = heapq.heappop(scoville)
        #     if first >= K :
        #         break            
        else :
            if scoville[0] < K :
                return -1
            else :
                break
    return answer