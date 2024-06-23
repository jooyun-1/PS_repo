# 땅의 높이를 모두 동일하게 만들어야 함
# N * M 의 집터
# 1. (i, j)의 가장 위에 있는 블록 제거하여 인벤토리에 넣는다. (2초)
# 2. 인벤토리에서 블록 하나 꺼내서 좌표 (i, j)의 가장 위에 있는 블록 위에 놓는다. (1초)
# 땅 고르기 최소 시간, 땅의 높이

import sys
N, M, B = map(int, sys.stdin.readline().split())
board = []
answer = sys.maxsize
for n in range(N) :
    line = list(map(int,sys.stdin.readline().split()))
    board.append(line)

for block in range(257) :
    exceed, lack = 0, 0
    for i in range(N) :
        for j in range(M) :
            if block < board[i][j] :
                exceed += board[i][j] - block
            else :
                lack += block - board[i][j]
    if exceed + B >= lack :
        if (exceed * 2) + lack <= answer :
            answer = (exceed * 2) + lack
            h = block
print(answer, h)