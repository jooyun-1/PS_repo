import sys

N = int(sys.stdin.readline())
answer = 0
for n in range(N) :
    word = sys.stdin.readline().rstrip()
    stack = []
    for w in word :
        if len(stack) == 0 :
            stack.append(w)
        else :
            if stack[-1] == w :
                stack.pop()
            else :
                stack.append(w)
    if len(stack) == 0 :
        answer += 1
print(answer)