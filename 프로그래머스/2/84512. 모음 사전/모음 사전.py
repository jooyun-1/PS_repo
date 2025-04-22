from itertools import product

def solution(word):
    answer = 1
    alphas = ['A','E','I','O','U']
    words = []
    for i in range(1,6) :
        temp = list(product(alphas,repeat=i))
        for t in temp :
            words.append(''.join(t))
    words.sort()
    for w in words :
        if w == word :
            break
        else :
            answer += 1
    
    return answer