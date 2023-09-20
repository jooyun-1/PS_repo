def solution(n, left, right):
    answer = []

    r1,c1 = left // n, (left % n)
    r2,c2 = right // n, (right % n)

    for i in range(left,right+1) :
        a = i // n
        b = i % n
        if a < b : a, b = b, a 
        answer.append(a+1)
    return answer