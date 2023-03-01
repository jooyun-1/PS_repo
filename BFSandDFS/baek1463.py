# X % 3 == 0 => 3으로 나눈다
# X % 2 == 0 => 2로 나눈다
# 1을 뺀다
# 연산을 하는 최소 횟수?
# bfs
import sys
# import time
# start = time.time()
N = int(sys.stdin.readline())
que = []
cnt = 0
visited = [0] * (N+1)
que.append(N)
while que :
    num = que.pop(0)
    if num == 1:
        cnt = visited[num]
        break
    if num % 3 == 0 :
        for i in (int(num//3), num -1) :
            if visited[i] == 0 and 0<=i<=N+1 :
                visited[i] = visited[num] + 1
                que.append(i)
    if num % 2 == 0 :
        for i in (int(num//2), num -1) :
            if visited[i] == 0 and 0<=i<=N+1 :
                visited[i] = visited[num] + 1
                que.append(i)
    else :
        i = num - 1
        if visited[i] == 0 and 0<=i<=N+1 :
                visited[i] = visited[num] + 1
                que.append(i)                   
print(cnt)
# end = time.time()
# print(end-start)

