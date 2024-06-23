from itertools import combinations
def solution(elements):
    answer = 0
    length = len(elements)
    sums = set()
    elements = elements * 2
    for i in range(length) :
        for j in range(length) :
            sums.add(sum(elements[j:j+i+1]))
    answer = len(sums)
    return answer