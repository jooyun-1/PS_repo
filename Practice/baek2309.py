import sys
from itertools import combinations
arr, answer = [], []
for i in range(9) :
    n = int(sys.stdin.readline())
    arr.append(n)
arr.sort()
combi = list(list(combinations(arr,7)))
answer = []
for i in range(len(combi)) :
    for j in range(len(combi[i])):
        if sum(combi[i]) == 100 :
            answer = combi[i]
            break
    if len(answer) > 0 :
        break
for i in range(len(answer)) :
    print(answer[i])