import sys
from collections import deque

# belt의 belt.count(0)이 K 이상이면 종료
# belt 순서대로 돌며 if belt[i] < 1 이어야 돌아감

N, K = map(int,sys.stdin.readline().split())
A = deque(list(map(int,sys.stdin.readline().split())))
answer = 0
belt = deque([False] * N)

while True :
    A.rotate(1)
    belt.rotate(1)
    answer += 1
    belt[N-1] = False
    for i in range(N-2,-1,-1) :
        if belt[i] and not belt[i+1] and A[i+1] > 0 :
            belt[i], belt[i+1] = False, True
            A[i+1] -= 1
    belt[N-1] = False

    if A[0] > 0 :
        belt[0] = True
        A[0] -= 1

    if A.count(0) >= K :
        break

print(answer)