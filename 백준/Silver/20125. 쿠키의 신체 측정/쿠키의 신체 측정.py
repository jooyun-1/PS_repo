import sys

n = int(sys.stdin.readline())

board = []
head = [0,0]

for i in range(n) :
    s = sys.stdin.readline().rstrip()
    board.append(s)
for i in range(n) :
    h_flag = False
    for j in range(n) :
        if board[i][j] == '*' :
            head = [i,j]
            h_flag = True
            break
    if h_flag :
        break

heart = [head[0]+1, head[1]]
print(head[0]+2, head[1]+1)

back,left_l,right_l = 0, 0, 0

left_h = board[heart[0]][:heart[1]].count('*')
right_h = board[heart[0]][heart[1]+1:].count('*')
for i in range(heart[0]+1, n) :
    if board[i][heart[1]] != '*' :
        last_back = [i,heart[1]]
        break
    else :
        back += 1
        
for i in range(last_back[0],n) :
    if board[i][heart[1]-1] == '*' :
        left_l += 1
    if board[i][heart[1]+1] == '*' :
        right_l += 1

print(left_h,right_h,back,left_l,right_l)



