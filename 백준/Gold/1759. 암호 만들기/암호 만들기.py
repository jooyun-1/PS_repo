import sys
from itertools import combinations

L, C = map(int,sys.stdin.readline().split())
arr = list(sys.stdin.readline().split())
combi = list(combinations(arr,L))
answer = []
for com in combi :
    flag = False
    flag2 = False
    cnt = 0
    for c in com :
        if c in ['a','e','i','o','u'] :
            flag = True
        elif c not in ['a', 'e', 'i', 'o', 'u']:
            cnt += 1
            if cnt >= 2:
                flag2 = True
    if flag == True and flag2 == True :
        temp = list(com)
        temp.sort()
        answer.append(''.join(temp))
answer.sort()
for ans in answer :
    print(ans)