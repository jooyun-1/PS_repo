import sys
import math

while True :
    n = int(sys.stdin.readline())
    if n == 0 :
        break
    cnt = 0
    for i in range(n+1, 2*n+1) :
        flag = True
        for j in range(2,int(math.sqrt(2*n))+1) :
            # print(i,j)
            if i == 1 :
                break
            if i % j == 0 :
                flag = False
                break
        if flag :
            # print('f',i)
            # print(math.sqrt(int(math.sqrt(26))))
            cnt += 1
    print(cnt)