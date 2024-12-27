def solution(number, k):
    answer = []
    for n in number :
        while k > 0 and answer and answer[-1] < n :
            answer.pop()
            k -= 1
        answer.append(n)
    if k > 0 :
        answer = answer[:-k]
    return ''.join(answer)