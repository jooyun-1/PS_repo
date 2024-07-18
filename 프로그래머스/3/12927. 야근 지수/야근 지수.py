# 시작한 시점 += 남은 작업량 ** 2
# 1시간의 작업량 1
import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0
    answer = 0
    works = [-w for w in works]
    heapq.heapify(works)
    while n > 0:
        max_val = heapq.heappop(works)
        heapq.heappush(works, max_val+1)
        n -= 1

    for w in works:
        answer += w ** 2
    return answer