import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()

cnt = i = answer = 0

while i < (m-2) :
    if s[i:i+3] == 'IOI' :
        i += 2
        cnt += 1
        if cnt == n :
            answer += 1
            cnt -= 1
    else :
        i += 1
        cnt = 0
print(answer)