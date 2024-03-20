def solution(weights):
    answer = 0
    weights_counter = dict()
    for w in weights :
        if w in weights_counter :
            weights_counter[w] += 1
        else :
            weights_counter[w] = 1
    for k, v in weights_counter.items() :
        if v >= 2 :
            answer += (v * (v-1)) // 2
    weights = set(weights)
    for w in weights :
        if w * 3/2 in weights :
            answer += weights_counter[w*3/2] * weights_counter[w]
        if w * 4/2 in weights :
            answer += weights_counter[w*4/2] * weights_counter[w]
        if w * 3/4 in weights :
            answer += weights_counter[w*3/4] * weights_counter[w]
            
    return answer