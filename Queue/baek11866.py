import sys
from collections import deque

n, k = map(int,sys.stdin.readline().split())
arr = [i for i in range(1,n+1)]
que = deque(arr)
answer = "<"

while que :
    que.rotate(-(k-1))
    a = que.popleft()
    answer += str(a) + ", " 
answer = answer[:-2]
print(answer + ">")

