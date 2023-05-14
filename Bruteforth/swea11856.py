t = int(input())

for test in range(1,t+1) :
    s = input().rstrip()
    flag = True
    for i in range(len(s)) :
        if s.count(s[i]) == 2 :
            pass
        else :
            flag = False
            break
    if flag == False :
        print('#{} {}'.format(test,'No'))
    else :
        print('#{} {}'.format(test,'Yes'))