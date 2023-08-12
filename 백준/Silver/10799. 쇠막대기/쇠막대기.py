# 1. Summary
# 레이저를 위에서 수직으로 발사하여 막대기를 자른다
# 1) 자신보다 긴 쇠막대기 위에만 놓일 수 있음
# 2) 완전히 포함되도록 놓되, 끝점은 안 겹치게 놓는다.
# 3) 각 쇠막대기를 자르는 레이저는 적어도 하나 존재
# 4) 레이저는 어떤 쇠막대기의 양 끝점과도 안 겹침

# 2.
# () => '*', stack에 ( 만나면 add, ) 만나면 pop
# index차이로 길이 구하고, 이 안의 * 개수 + 1

# 레이저 = '()' 쇠막대기 양쪽 끝 : '(.........)'
import sys
s = sys.stdin.readline().rstrip()
s = s.replace('()','*')
stack = []
answer = 0
for i in range(len(s)) :
    if s[i] == '(' :
        stack.append([i,s[i]])
    elif s[i] == ')' :
        index, ch = stack.pop()
        dist = i - index
        cnt = s[index:i+1].count("*")
        answer += (cnt + 1)
print(answer)