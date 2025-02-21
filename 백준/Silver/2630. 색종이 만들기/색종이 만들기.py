import sys

n = int(sys.stdin.readline())
board = []
white, blue = 0, 0

for i in range(n) :
    line = list(map(int,sys.stdin.readline().split()))
    board.append(line)

def count_paper(x,y,size) :
    paper = board[x][y]
    single_color = True
    global white, blue
    for i in range(x,x+size) :
        for j in range(y,y+size) :
            if board[i][j] != paper :
                single_color = False
                break
        if not single_color :
            break
    if single_color :
        if paper == 0 :
            white += 1
        else :
            blue += 1
        return
    half = size // 2
    count_paper(x, y, half)  # 1사분면 (왼쪽 위)
    count_paper(x, y + half, half)  # 2사분면 (오른쪽 위)
    count_paper(x + half, y, half)  # 3사분면 (왼쪽 아래)
    count_paper(x + half, y + half, half)  # 4사분면 (오른쪽 아래)

count_paper(0,0,n)

print(white)
print(blue)