from itertools import combinations
def solution(t, p):
    answer = 0
    index = 0
    temp = []
    while index + len(p) <= len(t) :
        temp.append(t[index : index + len(p)])
        index +=1
    for item in temp :
        if item <= p :
            answer += 1
    return answer