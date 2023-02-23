import sys
N = int(input())
stack, answer= [], []
for i in range(N) :
    s = sys.stdin.readline().split()
    cmd = s[0]
    if len(s) > 1 :
        data = int(s[1])
    if cmd == 'push' :
        if data :
            stack.append(data)
    if cmd == 'top' :
        if len(stack) > 0 :
            answer.append(stack[-1])
        else :
            answer.append(-1)
    if cmd == 'size' :
        answer.append(len(stack))
    if cmd == 'empty' :
        if len(stack) == 0 :
            answer.append(1)
        else :
            answer.append(0)
    if cmd == 'pop' :
        if len(stack) > 0 :
            answer.append(stack.pop())
        else :
            answer.append(-1)
for ans in answer :
    print(ans)