t = int(input())

for test in range(1,t+1) :
    P, Q = input().rstrip(), input().rstrip()
    if P + "a" != Q :
        print('#{} {}'.format(test, 'Y'))
    else :
        print('#{} {}'.format(test, 'N'))
