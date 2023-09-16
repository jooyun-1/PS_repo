# 같은 알파벳 2개 붙어 있는 짝 찾는다.
# 둘을 제거하고 앞 뒤로 이어 붙힌다.
def solution(s):
    answer = 0
    if len(s) % 2 == 1 :
        return 0
    stack = [s[0]]
    for i in range(1,len(s)) :
        if len(stack) > 0 and stack[-1] == s[i] :
            stack.pop()
        else :
            stack.append(s[i])
    if len(stack) == 0 :
        answer = 1
    return answer