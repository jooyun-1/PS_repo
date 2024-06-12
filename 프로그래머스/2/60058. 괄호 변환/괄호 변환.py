def checkRight(s) :
    stack = []
    for i in range(len(s)) :
        if s[i] == '(' :
            stack.append(s[i])
        if s[i] == ')' :
            if len(stack) == 0 :
                return False
            else :
                stack.pop()
    if len(stack) > 0 :
        return False
    else :
        return True
    
def divide(s) :
    left, right = 0, 0
    for i in range(len(s)) :
        if s[i] == '(' :
            left += 1
        if s[i] == ')' :
            right += 1
        if left == right :
            return s[:i+1], s[i+1:]

def solution(p):
    answer = ''
    
    if len(p) == 0 :
        return ""
    u, v = divide(p)
    
    if checkRight(u) :
        return u + solution(v)
    else :
        answer = '(' + solution(v) + ')'

        for s in u[1:len(u)-1]:
            if s == '(':
                answer += ')'
            else:
                answer += '('
        return answer
