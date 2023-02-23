# 2원, 5원 => 거스름돈 , 동전의 개수: 최소

rest = int(input())
cnt = 0
while True :
    if rest % 5 == 0 :
        cnt += rest // 5
        break
    else : 
        rest -= 2
        cnt += 1
    if rest < 0 :
        break
if rest < 0:
    print(-1)
else :
    print(cnt)
