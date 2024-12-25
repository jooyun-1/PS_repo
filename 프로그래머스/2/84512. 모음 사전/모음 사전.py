from itertools import permutations
from itertools import product
def solution(word):
    answer = 1
    dictionary = ['A', 'E', 'I', 'O', 'U']
    word_list = list()
    for i in range(1,6) :
        temp = list(product(dictionary,repeat = i))
        for perm in temp :
            word_list.append(''.join(perm))
    word_list.sort()
    for w in word_list :
        if w == word :
            break
        else :
            answer += 1
    return answer