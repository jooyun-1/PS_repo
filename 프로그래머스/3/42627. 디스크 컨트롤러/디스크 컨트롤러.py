import heapq

def solution(jobs):
    answer = 0
    finish = 0
    before = -1
    heap = []
    now = 0
    while finish < len(jobs) :
        for job in jobs :
            if before < job[0] <= now :
                heapq.heappush(heap,(job[1],job[0]))
        if len(heap) > 0 :
            now_working = heapq.heappop(heap)
            before = now
            now += now_working[0]
            answer += (now - now_working[1])
            finish += 1
        else :
            now += 1
    answer = int(answer/len(jobs))
    return answer