s = input().rstrip().split('-')
num = []

for i in s :
    temp = i.split('+')
    sum = 0
    for t in temp :
        sum += int(t)
    num.append(sum)
answer = num[0]
for i in range(1,len(num)) :
    answer -= num[i]
print(answer)


