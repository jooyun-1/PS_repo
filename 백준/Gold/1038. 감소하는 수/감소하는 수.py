from itertools import combinations

N = int(input())
arr = []
for i in range(1,11) :
    for com in combinations(range(0,10),i) :
        com = list(com)
        com.sort(reverse=True)
        arr.append(int(''.join(map(str,com))))
arr.sort()

if N >= len(arr) :
    print(-1)
else :
    print(arr[N])