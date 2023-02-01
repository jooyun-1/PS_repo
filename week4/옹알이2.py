# aya, ye, woo, ma 
# 위 4개와 4개 조합한 발음 (연속해서 같은 발음 X)
from itertools import permutations
def solution(babbling):
    answer = 0
    arr = ["aya","ye","woo","ma"]
    repeat = ["ayaaya","yeye","woowoo","mama"]
    for bab in babbling :
        for word in repeat :
            bab = bab.replace(word,"X")
        for word in arr :
            bab = bab.replace(word,"O")
        flag = True
        for ch in bab :
            if ch != "O":
                flag = False
                break
        if flag == True:
            answer += 1
    return answer