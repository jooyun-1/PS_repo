import sys
from collections import deque
# 8개의 톱니(N극, S극 나타냄)를 가지는 톱니바퀴 4개
# 톱니바퀴에는 번호있음(1,2,3,4)
# 시계방향, 반시계방향 중 하나로 K번 회전
# 맞닿은 톱니의 극이 다르면, B는 A의 회전방향 반대로 회전
deq = [deque(list(map(int,sys.stdin.readline().rstrip()))) for _ in range(4)]

K = int(sys.stdin.readline())

for k in range(K) :
    arr = []
    for i in range(4) :
        arr.append([deq[i][6], deq[i][2]])
    n, d = map(int,sys.stdin.readline().split())
    n = n - 1
# 왼쪽 톱니
    if n != 0 :
        for a in range(n,0,-1) :
            if arr[a][0] != arr[a-1][1] :
                if (n - (a - 1)) % 2 == 0 :
                    deq[a-1].rotate(d)
                elif (n - (a - 1)) % 2 != 0 :
                    deq[a-1].rotate(-1*d)
            elif arr[a][0] == arr[a - 1][1]:
                break
# 오른쪽 톱니
    if n != 3 :
        for a in range(n,3) :
            if arr[a][1] != arr[a+1][0] :
                if (n - (a + 1)) % 2 == 0 :
                    deq[a+1].rotate(d)
                elif (n - (a + 1)) % 2 != 0 :
                    deq[a+1].rotate(-1 * d)
            elif arr[a][1] == arr[a+1][0] :
                break
    deq[n].rotate(d)
    
answer = 0
if deq[0][0] == 1 :
    answer += 1
if deq[1][0] == 1 :
    answer += 2
if deq[2][0] == 1 :
    answer += 4
if deq[3][0] == 1 :
    answer += 8
print(answer)