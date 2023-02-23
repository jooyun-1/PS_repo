# n일, W: 초기 현금

n, w = map(int, input().split())
price = []
coin = 0
flag = 'desc'
for i in range(n) :
    price.append(int(input()))

for i in range(len(price)) :
    if i == len(price) -1 :
        w += coin * price[i]
        break
    if price[i+1] > price[i] :
        if flag == 'desc' :
            coin += int(w//price[i])
            w -= coin * price[i]
            flag = 'asc'
            
        flag = 'asc'
    
    if price[i+1] < price[i]:
        if flag == 'asc' :
            w += coin * price[i]
            coin = 0
            flag = 'desc'
            
        flag = 'desc'
print(w)