# s = s + s = 2s
# s = s - s = 0
# s = s * s = s ** 2
# s = s / s = 1 (s != 0)
import sys
s, t = map(int, sys.stdin.readline().split())
que= list()
visited = []
new = 0
answer = ''
if s == t :
    print(0)
    sys.exit()

def bfs(s) :
    answer = ''
    que.append([s,answer])
    while que :
        s, answer = que.pop(0)
        if s == t :
            return answer
        for cal in ('*', '+', '-', '/') :
            if cal == '*' :
                new = s * s
            elif cal == '+' :
                new = s + s
            elif cal == '/' :
                if s != 0 :
                    new = 1
            if new not in visited and 0<= new <= t  :
                que.append([new, answer + cal])
                visited.append(new)
    return -1
print(bfs(s), end = "")

