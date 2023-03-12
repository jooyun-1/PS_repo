# 길이
# A의 모든 자리수의 합 + B의 모든 자리수의 합 중 작은 합
# 사전 순 비교
import sys
N = int(sys.stdin.readline())
serial = []
for i in range(N) :
    sum = 0
    num = sys.stdin.readline()
    for j in num :
        if j.isdigit() :
            sum += int(j)
    serial.append((num , sum))

serial = list(sorted(serial, key = lambda x : (len(x[0]), x[1], x[0])))
for s in serial :
    print(s[0], end="")