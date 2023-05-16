t = int(input())

for test in range(1,t+1) :
    D, L, N = map(int,input().split())
    sum = D
    for i in range(N-1) :
        sum += D*((1+i) * L / 100)
        sum += D
    print('#{} {}'.format(test,int(sum)))
    