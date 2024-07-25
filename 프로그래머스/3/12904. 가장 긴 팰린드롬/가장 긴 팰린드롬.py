def solution(s):
    answer = 0
    for i in range(len(s)) :
        for j in range(len(s),-1,-1) :
            new_s = s[i:j]
            if new_s == new_s[::-1] :
                answer = max(answer,len(new_s))
    return answer