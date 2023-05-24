import sys
from collections import deque

n, k = map(int,sys.stdin.readline().split())
arr, answer = [], []
for i in range(1,n+1) :
    arr.append(i)
deq = deque(arr)
while deq :
    deq.rotate(-k+1)
    temp = deq.popleft()
    answer.append(temp)
print('<', end='')
for i2 in range(len(answer)) :
    if i2 == len(answer) - 1 :
        print(answer[i2], end= '')
        print('>')
    else : 
        print(answer[i2], end=', ')