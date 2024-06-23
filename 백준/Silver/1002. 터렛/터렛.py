import sys

T = int(sys.stdin.readline())

for t in range(T) :
    x1, y1, r1, x2, y2, r2 = map(int,sys.stdin.readline().split())
    d = (x2-x1)**2 + (y2-y1)**2
    answer = 0
    if d == 0 :
        if r1 == r2 :
            answer = -1
        else :
            answer = 0
    else :
        if (r2 - r1) ** 2 <  d < (r1 + r2) ** 2 :
            answer = 2
        elif d == (r1 + r2) ** 2 or abs(r2 - r1) ** 2  == d :
            answer = 1
        else :
            answer = 0
    print(answer)