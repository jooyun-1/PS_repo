# 길이 짧은 것
# 같으면, 모든 자리 수의 합이 작은 것 (숫자만 더함)
# 위가 다 같으면, 사전순 비교
import sys
N = int(sys.stdin.readline())
serial = []

def swap(a, b) :
    temp = a
    a = b
    b = temp
    return [a,b]

for i in range(N) :
    line = sys.stdin.readline()
    sum = 0
    for j in line :
        if j.isdigit() :
            sum += int(j)
    serial.append((line,sum))

serial = list(sorted(serial,key = lambda x: (len(x[0]), x[1], x[0])))
for s in serial :
    print(s[0], end = "")



