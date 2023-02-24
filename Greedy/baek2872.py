# 책 알파벳 순서 정렬
# 사전 순 가장 앞서는 책 => 가장 위, 뒤에 있는 책 => 밑 (1~N)
# 방법 : 책 하나를 빼고 가장 위에 놓는 것
# arr[0]이 arr[1]보다 크면
#from collections import deque
import sys

N = int(sys.stdin.readline())

cnt = 0
arr = []

for i in range(N) :
    arr.append(int(sys.stdin.readline()))
target = N
for i in range(N-1,-1,-1) :
    if arr[i] != target :
        cnt += 1
    else :
        target -= 1
