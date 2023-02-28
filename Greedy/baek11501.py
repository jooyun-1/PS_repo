# 주식 하나 buy
# 원하는 만큼 주식 sell
# 아무것도 안함
# => 최대 이익 낼 수 있는 법
import sys

T = int(sys.stdin.readline())
profits = []
for i in range(T) :
    N = int(sys.stdin.readline())
    prices = list(map(int,sys.stdin.readline().split()))
    profit, max_price = 0, 0
    target = [0] * len(prices)
    for j in range(N-1,-1,-1) :
         max_price = max(max_price,prices[j])
         target[j] = max_price
    for k in range(N) :
         profit += target[k] - prices[k]
    
    if profit < 0 :
         profits.append(0)
    else :
         profits.append(profit)

for pro in profits :
     print(pro)

        

