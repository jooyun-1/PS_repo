def solution(n):
    answer = 0
    start = 1
    while True :
        total = 0
        if start > 10000 :
            break
        for i in range(start, 10001) :
            total += i
            if total == n :
                answer += 1
            elif total > n :
                break
        start += 1
        
    return answer