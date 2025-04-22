# 작업의 소요시간이 짧은 것, 작업의 요청 시각이 빠른 것, 작업의 번호가 작은 것
import heapq

def solution(jobs):
    answer = 0
    before = -1
    now, finish = 0, 0
    heap = []
    
    while finish < len(jobs) :
        for job in jobs :
            if before < job[0] <= now :
                heapq.heappush(heap,(job[1],job[0]))
        if len(heap) > 0 :
            time, req = heapq.heappop(heap)
            before = now
            now += time
            answer += (now-req)
            finish += 1
        else :
            now += 1
    return answer // len(jobs)