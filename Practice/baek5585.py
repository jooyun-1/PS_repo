num = int(input())
money = [500,100,50,10,5,1]
rest = 1000 - num
cnt = 0
for i in range(len(money)) :

    cnt += rest // money[i]
    rest %= money[i]

print(cnt)