t = int(input())

for test in range(1,t+1) :
    n = int(input())
    cnt = 0
    flag = 'Bob'
    if n % 2 != 0 :
        print('#{} {}'.format(test,'Bob'))
    else :
        print('#{} {}'.format(test,'Alice'))      

