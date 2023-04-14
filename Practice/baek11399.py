import sys
n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().rstrip().split()))
sum = 0
arr.sort()
for i in range(len(arr)-1,-1,-1) :
    for j in range(i,-1,-1) :
        sum += arr[j]
print(sum)
