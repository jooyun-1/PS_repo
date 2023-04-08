# 캠핑장 => 연속하는 P일 중 L일동안만 사용가능
# V일짜리 휴가
import sys
case = 1
answer = [] 
while True :
    l, p, v = map(int,sys.stdin.readline().split())
    if l == 0 and p == 0 and v == 0 :
        break
    temp = v // p
    result = temp * l + min(v % p, l)
    answer.append(["Case " + str(case) +': ' + str(result)])
    case += 1

for ans in answer:
    print(''.join(ans))