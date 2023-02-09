# 1~n 스택에 푸쉬 (오름차순으로)
# 4 3 6 8 7 5 2 1
# 1,2,3,4 => 3,4 => 1,2,5,6 =>1,2,5 => 1,2,5,7,8

n = int(input())
stack = []
answer = []
x = 1
flag = 1
for i in range(n) :
    num = int(input())
    while x <= num :
        stack.append(x)
        answer.append('+')
        x += 1
    if stack[-1] == num :
        stack.pop()
        answer.append('-')
    else :
        print('NO')
        flag = 0
        break
if flag == 1 :
    for i in answer :
        print(i)

            








