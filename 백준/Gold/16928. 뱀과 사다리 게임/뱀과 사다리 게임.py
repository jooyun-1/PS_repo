from collections import deque

N, M = map(int,input().split())

ladders, snakes = dict(), dict()
dice = [1,2,3,4,5,6]
visited = [0] * 101
board = [0] * 101

for i in range(N) :
    x, y = map(int,input().split())
    ladders[x] = y
for i in range(M) :
    u, v = map(int,input().split())
    snakes[u] = v

que = deque([1])

while que :
    x = que.popleft()
    
    if x == 100 :
        print(board[x])
        break
    for i in dice :
        next = x + i
        if next <= 100 and visited[next] == 0:
            if next in ladders.keys() :
                next = ladders[next]
            if next in snakes.keys() :
                next = snakes[next]
            if visited[next] == 0 :
                que.append(next)
                board[next] = board[x] + 1
                visited[next] = 1
