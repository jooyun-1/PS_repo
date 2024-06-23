def solution(n):
    answer = ''
    while True :
        if n == 0 :
            break
        t = n % 3
        n = n // 3 
        if t == 0 :
            t = 4
            n -= 1
        answer += str(t)
    
    return ''.join(reversed(answer))