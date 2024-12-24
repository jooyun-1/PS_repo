def solution(brown, yellow):
    answer = []
    sum = brown + yellow
    for b in range(1, sum + 1) :
        if sum % b == 0 :
            a = sum // b
            if a >= b :
                if 2 * a + 2 * b == brown + 4 :
                    answer = [a,b]
    return answer