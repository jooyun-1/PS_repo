from collections import deque

def check(s) :
    stack = []
    stack.append(s[0])
    for i in range(1,len(s)) :
        if len(stack) == 0 :
            stack.append(s[i])
        elif s[i] == ']' :
            if stack[-1] == '[' :
                stack.pop()
        elif s[i] == ')' :
            if stack[-1] == '(' :
                stack.pop()
        elif s[i] == '}' :
            if stack[-1] == '{' :
                stack.pop()
        else :
            stack.append(s[i])
    if len(stack) == 0 :
        return True
    else :
        return False
    
def solution(s):
    answer = 0
    deq = deque(s)
    result = []
    for i in range(len(deq)) :
        for j in range(i+1) :
            c = deq.popleft()
            deq.append(c)
        if check(deq) == True :
            answer += 1
        deq = deque(s)

    return answer