# 한 계단 or 두 계단씩 오를 수 있다
# 연속된 세 개의 계단 불가능
# 도착 계단은 무조건 밟아야함
# 10,20, 25,10
# 10,20 25,20
# 10,15, 25,20
# 10,15 10,20

# DP
import sys
N = int(sys.stdin.readline())
score = [0]
DP = [0] * (N+1)
sum = 0
for i in range(1,N+1) :
    score.append(int(sys.stdin.readline())) 
if N == 1 :
    print(score[1])
elif N == 2 :
    print(score[1] + score[2])
else :
    DP[1] = score[1]
    DP[2] = DP[1]+score[2]
    for i in range(3,N+1) :
        DP[i] = max(score[i]+score[i-1]+DP[i-3],score[i]+DP[i-2])
    print(DP[N]) 
## 완전 탐색
# import sys
# import time
# start = time.time()
# N = int(sys.stdin.readline())
# score = [0] 
# for i in range(1,N+1) :
#     score.append(int(sys.stdin.readline())) 
# pos, sum = N, score[N]
# flag = False

# while pos >= 2:
#     if score[pos-1] > score[pos-2] :
#         # print('1',pos,sum)
#         if flag == False :
#             sum += score[i-1]
#             pos -= 1
#             flag = True
#     elif score[pos-1] < score[pos-2] :
#         # print('2',pos,sum)
#         sum += score[pos-2]
#         pos -= 2
#         flag = False
# print(sum)
# end = time.time()
# print(end - start)