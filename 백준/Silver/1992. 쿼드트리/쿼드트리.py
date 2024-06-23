# 흰점 : 0, 검은 점 : 1
import sys

N = int(sys.stdin.readline())
board = []
for n in range(N) :
    line = list(map(int,sys.stdin.readline().rstrip()))
    board.append(line)

def zipVideo(sr, sc, size) :
    temp = board[sr][sc]
    for r in range(sr, sr + size) :
        for c in range(sc, sc + size) :
            if board[r][c] != temp :
                temp = -1
                break
    if temp == -1 :
        print("(",end="")
        size = size // 2
        zipVideo(sr,sc,size)
        zipVideo(sr, sc + size, size)
        zipVideo(sr + size, sc , size)
        zipVideo(sr + size, sc + size, size)
        print(")",end ="")
    elif temp == 1 :
        print(1, end = "")
    else :
        print(0, end = "")
zipVideo(0,0,N)