t = int(input())

for test in range(1,t+1) :
    n = int(input())
    flag = False
    for i in range(1,10) :
        for j in range(1,10) :
            if n == i * j :
                flag = True
                break
        if flag == True :
            print('#{} {}'.format(test,'Yes'))
            break
    if flag == False :
            print('#{} {}'.format(test,'No'))
