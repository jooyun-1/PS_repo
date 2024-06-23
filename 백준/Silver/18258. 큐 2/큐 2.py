import sys
from collections import deque

N = int(sys.stdin.readline())

que,ans = deque(), []

for i in range(N) :
    arr = list(sys.stdin.readline().split())
    command = arr[0]
    if len(arr) > 1 :
        x = arr[1]
    if command == "push" :
        que.append(int(x))
    elif command == "pop" :
        if len(que) == 0 :
            ans.append(-1)
        else :
            num = que.popleft()
            ans.append(num)
    elif command == "size" :
        ans.append(len(que))
    elif command == "empty" :
        if len(que) == 0 :
            ans.append(1)
        else :
            ans.append(0)
    elif command == "front" :
        if len(que) == 0 :
            ans.append(-1)
        else :
            ans.append(que[0])
    elif command == "back" :
        if len(que) == 0 :
            ans.append(-1)
        else :
            ans.append(que[-1])
for an in ans:
    print(an)