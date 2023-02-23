# 알파벳 대,소문자, 숫자, 백스페이스, 화살표

N = int(input())
# <, - 를 만나면....
index = 0
answer = list()
for i in range(N) :
    password = input()
    left_stack, right_stack = list(), list()    # 커서의 왼쪽, 오른쪽을 나누고 Stack으로 저장

    for j in range(len(password)) :
        if password[j] == '<' :
            if left_stack :
                right_stack.append(left_stack.pop())
        elif password[j] == '>' :
            if right_stack :
                left_stack.append(right_stack.pop())
        elif password[j] == '-' :
            if left_stack :
                left_stack.pop()
        else :
            left_stack.append(password[j])
    left_stack.extend(list(reversed(right_stack)))  # 커서 오른쪽 stack은 반대 방향이므로 뒤집어서 붙혀줘야함.
    answer.append(''.join(left_stack))
for ans in answer :
    print(''.join(ans))