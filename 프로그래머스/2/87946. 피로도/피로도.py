# 최소 필요 피로도, 소모 피로도
from itertools import permutations

def solution(k, dungeons):
    answer = -1
    arr = list(permutations(dungeons,len(dungeons)))
    temp = k
    for perms in arr :
        cnt = 0
        k = temp
        for perm in perms :
            if k >= perm[0] :
                k -= perm[1]
                cnt += 1
            else :
                break
        answer = max(answer,cnt)
        
    return answer