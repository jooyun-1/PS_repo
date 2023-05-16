t = int(input())

for test in range(1,t+1) :
    a, b= 1, 1
    s = input()
    for i in range(len(s)) :
        if s[i] == 'L' :
            b = a+b
        elif s[i] == 'R' :
            a = a+b
    print('#{} {} {}'.format(test,a,b))