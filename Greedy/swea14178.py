t = int(input())

for test in range(1,t+1) :
    N, D = map(int, input().split())
    cnt = 0
    D = 2*D + 1
    if N % D == 0 :
        cnt += N // D
    else :
        cnt += N // D + 1
    print('#{} {}'.format(test,cnt))