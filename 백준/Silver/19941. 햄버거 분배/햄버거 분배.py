import sys

n, k = map(int,sys.stdin.readline().split())
s = list(sys.stdin.readline().rstrip())
answer = 0
for i in range(len(s)) :
    if s[i] == 'P' :
        for j in range(i-k,i+k+1) :
            if 0 <= j < n and s[j] == 'H' :
                answer += 1
                s[j] = 'E'
                break
print(answer)