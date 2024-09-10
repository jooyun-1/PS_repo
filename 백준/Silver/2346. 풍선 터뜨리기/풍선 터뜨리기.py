from collections import deque
import sys
N = int(sys.stdin.readline())
deq = deque(enumerate(map(int, sys.stdin.readline().split())))
result = []
while deq:
    num, i = deq.popleft()
    result.append(num+1)
    if i > 0:
        deq.rotate(-(i-1))
    else:
        deq.rotate(-i)
for j in result:
    print(j, end = ' ')