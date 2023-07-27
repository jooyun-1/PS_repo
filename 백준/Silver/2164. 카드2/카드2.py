import sys
from collections import deque

N = int(sys.stdin.readline())

arr = [i for i in range(1, N+1)]
deq = deque(arr)

while len(deq) > 1 :
    deq.popleft()
    # if len(deq) > 0 :
    top = deq.popleft()
    deq.append(top)

print(deq[0])