def solution(n):
    answer = 0
    count = str(bin(n)).count('1')
    
    while True :
        n += 1
        temp = str(bin(n))
        if temp.count('1') == count :
            answer = n
            break
    return answer