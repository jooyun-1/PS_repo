import sys
import math

n, k = map(int, sys.stdin.readline().split())

arr = [n for n in range(2,n+1)]
# 아직 지우지 않은 수 중 가장 작은 수 p
# p 지우고, 아직 지우지 않은 p의 배수를 크기 순서대로 지운다
remove_cnt = 0
for num in range(2,n+1) :
    cnt = 0
    for i in range(1, math.floor(math.sqrt(num))+1) :
        if num % i == 0 :
            cnt += 1
    if cnt == 1 :
        temp = num
        for j in range(temp, n+1) :
            if j % temp == 0 :
                if j in arr :
                    arr.remove(j)
                    remove_cnt += 1
                    if remove_cnt == k :
                        print(j)