t = int(input())

for test in range(1,t+1) :
    n = int(input())
    week = list(map(int,input().split()))
    cnt = 0
    answer = 0
    arr = []
    for a in range(len(week)) :
        if week[a] == 1 :
            arr.append(a)

    answer = 1e9
    
    for day in arr :
        dayCnt = 0
        classCnt = 0
        while classCnt < n :
            if week[day] == 1 :
                classCnt += 1
            dayCnt += 1
            if day > 5 :
                day = 0
            else :
                day += 1
        answer = min(answer, dayCnt)
        print(answer)
