# from itertools import permutations
from itertools import product
def solution(word):
    answer = 0
    dictionary = ['A','E','I','O','U']
    arr = []
    for i in range(1,6) :
        # temp = list(permutations(dictionary,i))
        temp = list(product(dictionary,repeat = i))
        for perm in temp :
            arr.append(''.join(perm))
    arr.sort()
    for a in arr :
        if a == word :
            answer += 1
            return answer
        answer += 1
    return answer