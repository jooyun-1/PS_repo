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
    while x <= num :    # 오름차순대로 stack에 push
        stack.append(x)
        answer.append('+')
        x += 1          # x => 이 때까지 stack에 들어간 숫자
    if stack[-1] == num : # stack의 Top이 입력 숫자와 같을 때 pop
        stack.pop()
        answer.append('-')
    else :                # 입력 숫자가 pop 될 수 없을 때 (Top값이 아닐 때)                        
        print('NO')
        flag = 0
        break
if flag == 1 :
    for i in answer :
        print(i)

            








