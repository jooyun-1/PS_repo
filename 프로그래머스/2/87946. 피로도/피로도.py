from itertools import permutations
def solution(k, dungeons):
    answer = -1
    perm = list(permutations(dungeons, len(dungeons)))
    
    
    for pe in perm :
        cur = k
        temp = 0
        for p in pe :
            min_val, val = p[0], p[1]
            if cur >= min_val :
                cur -= val
                temp += 1
            else :
                break
        answer = max(answer, temp)
    return answer