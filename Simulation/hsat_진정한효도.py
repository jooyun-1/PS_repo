import sys

board = []
possible_arr = []
for i in range(3) :
    line = list(map(int,sys.stdin.readline().split()))
    board.append(line)
    possible_arr.append(line)

for i in range(3) :
    temp = []
    for j in range(3) :
        temp.append(board[j][i])
    possible_arr.append(temp)
val = float('inf')
for pos in possible_arr :
    pos = list(set(pos))
    if len(pos) == 1 :
        val = 0
        break
    elif len(pos) == 2 :
        val = min(val,abs(pos[1]-pos[0]))
    else :
        val = min(val,2)
print(val)