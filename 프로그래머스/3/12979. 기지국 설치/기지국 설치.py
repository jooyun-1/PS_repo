import math
def solution(n, stations, w):
    answer = 0
    now = 1
    range = w + w + 1
    for s in stations :
        length = s - w - now
        if length > 0 :
            answer += math.ceil(length/range)
        now = s + w + 1
    if n >= now :
        answer += math.ceil((n-now+1)/range)
    
    return answer