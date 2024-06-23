from itertools import combinations

def solution(k, tangerine):
    answer = 0

    arr = [0] * (max(tangerine)+1)
    for i in range(len(tangerine)) :
        arr[tangerine[i]] += 1
    arr.sort(reverse=True)

    cnt = 0
    for i in range(len(arr)) :
        if cnt >= k :
            break
        cnt += arr[i]
        answer += 1

    return answer