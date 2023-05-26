arr = [n for n in range(1,10001)]
for i in range(1,10001) :
    temp = str(i)
    sum = 0
    for j in range(len(temp)) :
        sum += int(temp[j])
    sum += i
    if sum in arr :
        arr.remove(sum)
for i2 in arr :
    print(i2)