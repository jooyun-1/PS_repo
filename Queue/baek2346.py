# 1~N 풍선이 원형으로 놓여있음
# i-1 -> i -> i+1
# 각 풍선 안에는 종이 (-N<=정수<=N)
# 처음엔 1번, 다음은 종이의 정수만큼 이동 후, 터뜨림

from collections import deque
import sys
N = int(sys.stdin.readline())
deq = deque(enumerate(map(int, sys.stdin.readline().split())))
result = []
while deq:
    num, i = deq.popleft()
    result.append(num+1)
    if i > 0:
        deq.rotate(-(i-1))
    else:
        deq.rotate(-i)
for j in result:
    print(j, end = ' ')



# from collections import deque
# import sys
# N = int(sys.stdin.readline())
# num = list(map(int,sys.stdin.readline().split()))
# bal = dict()
# answer = []
# for i in range(1,len(num)+1) :
#     bal[num[i-1]] = i

# deq = deque(num)
# bomb = 1
# while deq :
#     bomb = deq.popleft()
#     answer.append(bal[bomb])
#     if bomb > 0 :
#         deq.rotate(-(bomb-1))
#         # print(deq)
#         # bomb = deq.popleft()
#     else :
#         deq.rotate(-bomb)
#         # print(deq)
#         # bomb = deq.popleft()
#         # print(bomb)
    

# for ans in answer :
#     print(ans, end= " ")