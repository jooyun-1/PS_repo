t = int(input())

arr = [20,40,60,80,100,120,140,160,180,200]

for test in range(1,t+1) :
    n = int(input())
    sum = 0
    for i in range(n) :
        x, y = map(int,input().split())
        temp = (x*x + y*y) ** 0.5
        if temp > 200 :
            continue
        point, p = 0, 0
        for a in arr :
            if temp < a :
                point = a
                break
        p = (220 - point) / 20
        sum += p
    print('#{} {}'.format(test,int(sum)))