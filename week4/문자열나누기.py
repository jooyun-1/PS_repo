def solution(s):
    answer = 0
    tmp = s[0]
    x_cnt = 0
    diff_cnt = 0
    for ch in s :
        if x_cnt == diff_cnt :
            answer += 1
            tmp = ch
        if tmp == ch :
            x_cnt += 1
        else :
            diff_cnt += 1
    return answer