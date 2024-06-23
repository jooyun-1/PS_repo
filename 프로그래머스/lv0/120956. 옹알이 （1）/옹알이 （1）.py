
def solution(babbling):
    answer = 0
    arr = ["aya","ye","woo","ma"]
    for i in range(len(babbling)) :
        for s in arr :
            if s in babbling[i] :
                babbling[i] = babbling[i].replace(s,"*")
        if all(ch == "*" for ch in babbling[i]) :
            answer += 1
    return answer