import sys

s = list(sys.stdin.readline().rstrip())
one_count = s.count('1') // 2
zero_count = s.count('0') // 2

temp = 0
for i in s :
    if temp == one_count :
        break
    if i == '1' :
        s.remove(i)
        temp += 1
s = s[::-1]
temp = 0
for i in s :
    if temp == zero_count :
        break
    if i == '0' :
        s.remove(i)
        temp += 1

for i in s[::-1] :
    print(i, end ='')

