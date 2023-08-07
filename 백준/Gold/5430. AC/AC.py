from collections import deque
import sys

T = int(sys.stdin.readline())
answer = []

for t in range(T) :
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    arr = deque(sys.stdin.readline().rstrip()[1:-1].split(','))
    flag = True
    rotate = 0
    if n == 0 :
        arr = deque()
    for s in p :
        if s == 'R' :
            rotate += 1

        elif s == 'D' :
            if arr :
                if rotate % 2 != 0 :
                    arr.pop()
                else :
                    arr.popleft()
            else :
                flag = False
                print('error')
                break

    if flag == True:
        if rotate % 2 != 0 :
            arr.reverse()
            print("[" + ",".join(arr) + "]")
        else :
            print("[" + ",".join(arr) + "]")