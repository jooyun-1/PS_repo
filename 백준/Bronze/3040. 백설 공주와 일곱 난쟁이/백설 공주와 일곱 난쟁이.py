from itertools import combinations
arr = []
for i in range(9) :
    num = int(input())
    arr.append(num)
combi = list(combinations(arr,7))
answer = []
for com in combi :
    if sum(com) == 100 :
        answer = com
for ans in answer :
    print(ans)