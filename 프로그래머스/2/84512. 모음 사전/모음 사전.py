from itertools import product
def solution(word):
    words = []
    answer = 0
    arr = ['A', 'E', 'I', 'O', 'U']
    for i in range(1, 6):
        for p in product(arr, repeat=i):
            words.append(''.join(list(p)))
    words.sort()
    return words.index(word) + 1