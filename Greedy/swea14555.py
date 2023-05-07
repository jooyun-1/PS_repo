t = int(input())

for test in range(1,t+1) :
    str = input()
    cnt = 0
    for i in range(len(str)) :
        if str[i] == '(' :
            if str[i+1] == ')':
                cnt += 1
            else :
                cnt += 1
        elif str[i] == ')' :
            if str[i-1] != '(' :
                cnt += 1
    print('#{} {}'.format(test,cnt))