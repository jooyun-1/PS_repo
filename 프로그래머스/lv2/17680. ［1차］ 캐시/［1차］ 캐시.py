from collections import deque
from collections import defaultdict

def solution(cacheSize, cities):
    answer = 0
    deq = deque([])
    dic = defaultdict(int)
    
    if cacheSize == 0 :
        answer += 5 * len(cities)
    for c in cities :
        c = c.upper()
        if c in deq :
            deq.remove(c)
            deq.append(c)
            answer += 1
        elif c not in deq and len(deq) == cacheSize and len(deq) > 0 :
            deq.popleft()
            deq.append(c)
            answer += 5
        elif c not in deq and len(deq) < cacheSize :
            deq.append(c)
            answer += 5
    return answer