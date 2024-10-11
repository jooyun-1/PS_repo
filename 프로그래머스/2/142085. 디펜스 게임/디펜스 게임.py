import heapq

def solution(n, k, enemy):
    answer = 0
    pq = []
    sumEnemy = 0
    for e in enemy :
        sumEnemy += e
        heapq.heappush(pq,-e)
        if sumEnemy > n :
            if k == 0 :
                break
            else :
                sumEnemy += heapq.heappop(pq)
                k -= 1
        answer += 1
    return answer