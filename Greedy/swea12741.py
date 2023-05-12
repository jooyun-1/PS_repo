t = int(input())
answer = ''
for test in range(1,t+1) :
    a,b,c,d = map(int,input().split())

    start = max(a,c)
    end = min(b,d)
    if start > end :
        answer += f'#{test} {0}\n'
    else :
        answer += f'#{test} {end-start}\n'
print(answer,end='')    