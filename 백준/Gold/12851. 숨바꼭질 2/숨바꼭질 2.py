# 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
# 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동

import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
# 수빈, 동생
way = [0] * 100001
que = deque()
que.append(n)
result, cnt = 0, 0
while que:
    a = que.popleft()
    if a == k: # 둘이 만났을 때
        result = way[a] # 결과
        cnt += 1 # 방문 횟수 +1
        continue
    for i in [a-1, a+1, 2*a] :
        if 0 <= i < 100001 and (way[i] == 0 or way[i] == way[a] + 1) :
            way[i] = way[a] + 1
            que.append(i)
print(result)
print(cnt)
     
