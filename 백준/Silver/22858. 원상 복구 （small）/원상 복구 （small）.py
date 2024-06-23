import sys
import copy

N, K = map(int, sys.stdin.readline().split())

after = list(map(int,sys.stdin.readline().split()))
arrange = list(map(int,sys.stdin.readline().split()))
d = dict()
answer = [0] * N
for i in range(1, N + 1) :
    d[arrange[i-1]] = i

for k in range(K) :
    for i in range(1, N + 1) :
        answer[i-1] = after[d[i]-1]
    after = copy.deepcopy(answer)

for ans in answer :
    print(ans, end = " ")