from itertools import permutations

def solution(k, dungeons):
    answer = -1
    perm = list(permutations(dungeons,len(dungeons)))
    for per in perm :
        cnt = 0
        temp = k
        for p in per :
            if temp >= p[0] :
                temp -= p[1]
                cnt += 1
            else :
                break
        answer = max(cnt,answer)
    return answer