def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    index = 0
    for a in A :
        if a < B[index] :
            answer += 1
            index += 1
    
    return answer