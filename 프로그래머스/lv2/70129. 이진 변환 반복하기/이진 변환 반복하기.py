# 1. summary
# x = 0,1로 이루어짐
# 이진 변환
# 1) x의 모든 0 제거 2) x의 길이가 c면, x를 "c를 2진법으로 표현한 문자열"로 바꾼다
# 이진 변환 횟수와 제거된 모든 0의 개수
# 2. for문으로 돌면서 0 제거 후, 이진 변환

def solution(s):
    answer = [0,0]
    length = len(s)
    arr = list(s)
    loop_cnt = 0
    while (True) :
        cnt = 0
        if s == '1' :
            break
        for ch in s :
            if ch == '0' :
                cnt += 1
        answer[1] += cnt
        answer[0] += 1
        s = '1' * (len(s) - cnt)
        temp = len(s)
        s = bin(temp)[2:]
    return answer