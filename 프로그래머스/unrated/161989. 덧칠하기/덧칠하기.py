# 1. summary
# n미터 벽 => 테이프로 붙였다가 철거할 때 페인트 벗겨짐 => 덧칠 계획
# 구역을 나누어 일부만 새로 칠함 => 벽을 1m길이의 구역 n개로 나눔 (1~n)
# 롤러의 길이 : m미터 => 벽에서 벗어나면 안됨, 구역의 일부분만 포함되도록 칠하면 안됨
# 롤러로 페인트칠 횟수 최소화

# 2. 풀이
# 1234 2345 3456 4567 5678
import copy

def solution(n, m, section):
    answer = 0
    i = 0
    cur = section[0]
    while i < len(section) and cur <= n :
        if cur <= section[i] :
            answer += 1
            cur = section[i] + m
        else :
            i += 1
    return answer