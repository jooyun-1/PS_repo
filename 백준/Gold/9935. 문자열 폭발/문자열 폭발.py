s = input().rstrip()
bomb = input().rstrip()

stack = []
ex_len = len(bomb)
for i in range(len(s)) :
    stack.append(s[i])
    if ''.join(stack[-ex_len:]) == bomb :
        for j in range(len(bomb)) :
            stack.pop()
if stack :
    print(''.join(stack))
else :
    print('FRULA')

