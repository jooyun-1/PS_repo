def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i,val in enumerate(citations) :
        if i >= val :
            return i
    return len(citations)