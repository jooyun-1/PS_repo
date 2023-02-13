# 알파벳 대,소문자, 숫자, 백스페이스, 화살표

N = int(input())
# <, - 를 만나면....
index = 0
answer = list()
for i in range(N) :
    password = input()
    left_stack, right_stack = list(), list()

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
    left_stack.extend(list(reversed(right_stack)))
    answer.append(''.join(left_stack))
for ans in answer :
    print(''.join(ans))