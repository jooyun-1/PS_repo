import heapq
def solution(n, k, enemy):
    answer = 0
    sumEnemy = 0
    heap = []
    for e in enemy :
        heapq.heappush(heap,-e)
        sumEnemy += e
        if sumEnemy > n :
            x = heapq.heappop(heap)
            if k > 0 :
                k -= 1
                sumEnemy += x
            else :
                break
        answer += 1
    return answer