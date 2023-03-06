# 잘못된 수를 부를 때, 0을 외침 => 가장 최근 수 지움
# 받아 적은 모든 수의 합
import sys
K = int(sys.stdin.readline())
arr = []
for i in range(K) :
    num = int(sys.stdin.readline())
    if num != 0 :
        arr.append(num)
    if num == 0 :
        if len(arr) > 0 :
            arr.pop()
print(sum(arr))
