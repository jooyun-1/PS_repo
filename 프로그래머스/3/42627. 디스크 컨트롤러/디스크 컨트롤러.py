import heapq

def solution(jobs):
    answer = 0
    finish = 0
    before = -1
    now = 0
    heap = []
    while finish < len(jobs) :
        for job in jobs :
            if before < job[0] <= now : 
                heapq.heappush(heap, (job[1],job[0]))
        if len(heap) > 0 :
            time, req = heapq.heappop(heap)
            before = now
            now += time
            answer += (now - req)
            finish += 1
        else :
            now += 1
    

    return answer // len(jobs)