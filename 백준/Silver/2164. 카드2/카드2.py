from collections import deque

n = int(input())
deq = deque([i for i in range(1,n+1)])

while True :
    if len(deq) > 1 :
        first = deq.popleft()
        if len(deq) > 1 :
            second = deq.popleft()
            deq.append(second)
    else :
        answer = deq.popleft()
        break
print(answer)