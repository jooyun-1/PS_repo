def solution(elements):
    answer = 0
    length = len(elements)
    elements = elements * 2
    sums = set()
    for i in range(length) :
        for j in range(length) :
            sums.add(sum(elements[j:j+i+1]))
    return len(sums)