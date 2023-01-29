def solution(k, score):
    answer = []
    temp = []
    for sc in score :
        temp.append(sc)
        temp = sorted(temp, reverse = True)
        if len(temp) < k:
            answer.append(temp[-1])
        else:
            answer.append(temp[k-1])
    return answer