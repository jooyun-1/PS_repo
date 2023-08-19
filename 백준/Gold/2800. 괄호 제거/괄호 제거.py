# 괄호를 제거해서 나올 수 있는 서로 다른 식의 개수
# 쌍이 되는 괄호끼리 제거해야함
import sys
from itertools import combinations
line = sys.stdin.readline().rstrip()
answer = set()
left, right = [], []
for i in range(len(line)) :
    if line[i] == '(' :
        left.append(i)
    elif line[i] == ')' :
        right.append([left.pop(),i])
for i in range(1, len(right)+1) :
    combi = list(combinations(right,i))
    for com in combi :
        arr = list(line)
        for c in com :
            arr[c[0]] = ""
            arr[c[1]] = ""
        answer.add(''.join(arr))

for ans in sorted(answer) :
    print(ans)


