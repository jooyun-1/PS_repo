
def solution(babbling):
    answer = 0
    arr = ["aya","ye","woo","ma"]
    
    for i in range(len(babbling)) :
        for a in arr :
            if a in babbling[i] :
                babbling[i] = babbling[i].replace(a,'*')               
        if all(char == '*' for char in babbling[i]) :
            answer += 1
    return answer