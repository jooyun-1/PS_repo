import sys
n = sys.stdin.readline().rstrip()
arr = []
sum = 0
for i in range(len(n)) :
    arr.append(n[i])
    sum += int(n[i])
arr.sort(reverse=True)
if sum % 3 != 0 or '0' not in n :
    print(-1)
else :
    print(''.join(arr))

