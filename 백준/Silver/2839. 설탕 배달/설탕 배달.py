# N킬로그램 배달
# 봉지 -> 3kg, 5kg
# 최대한 적은 봉지
import sys
N = int(sys.stdin.readline())

res = N % 5
answer = 0
while N >= 0 :
    if N % 5 == 0 :
        answer += N // 5
        print(answer)
        break
    N -= 3
    answer += 1
else :
    answer = -1
    print(answer)