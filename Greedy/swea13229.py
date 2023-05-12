t = int(input())

week = {"MON" : 1 , "TUE" : 2 , "WED" : 3, "THU": 4, "FRI" : 5, "SAT" : 6, "SUN" : 7}

for test in range(1,t+1) :
    s = input()
    if s == "SUN" :
        print("#{} {}".format(test,7))
    else :
        print("#{} {}".format(test,7-week[s]))
    