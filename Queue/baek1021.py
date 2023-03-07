# N <=50, 1 <= M <= N, 1<= 위치 <= N
import sys
from collections import deque
N, M= map(int,sys.stdin.readline().split())
deq = deque([i for i in range(1,N+1)])
pos = list(map(int,sys.stdin.readline().split()))
cnt = 0
for p in pos :
    while True :
        if p == deq[0] :
            deq.popleft()
            break
        elif p != deq[0] :
            next = min(deq.index(p), abs(deq.index(p) - (len(deq)-1)))
            if next == deq.index(p) :
                deq.append(deq.popleft())
                cnt += 1
            elif next == abs(deq.index(p) - (len(deq)-1)) :
                deq.appendleft(deq.pop()) 
                cnt += 1
print(cnt)