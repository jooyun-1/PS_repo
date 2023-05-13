t =int(input())

for test in range(1,t+1) :
    a, b = map(int, input().split())
    if a + b < 24 :
        answer = a + b
    elif a + b == 24 :
        answer = 0
    else :
        answer = a + b - 24
    print('#{} {}'.format(test,answer))
