import sys
from collections import deque
import copy
from itertools import combinations
N, M, D = map(int, sys.stdin.readline().split())
board = []
anchor = list(combinations([i for i in range(M)],3))
dx = [0,-1,0]
dy = [-1,0,1]
for n in range(N) :
    line = list(map(int, sys.stdin.readline().split()))
    board.append(line)

def attack(arrow) :
    temp = [x[:] for x in board]
    attacked = [[0] * M for _ in range(N)]
    result = 0

    for i in range(N-1,-1,-1) :
        arr = []
        for a in arrow :
            deq = deque([(i,a,1)])

            while deq :
                x, y, d = deq.popleft()

                if temp[x][y] == 1 :
                    arr.append((x, y))
                    if attacked[x][y] == 0 :
                        attacked[x][y] = 1
                        result += 1
                    break
                if d < D :
                    for k in range(3) :
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < N and 0 <= ny < M :
                            deq.append((nx,ny,d+1))
        for x,y in arr :
            temp[x][y] = 0
    return result
answer = 0
for arrow in anchor :
    answer = max(answer, attack(arrow))
print(answer)