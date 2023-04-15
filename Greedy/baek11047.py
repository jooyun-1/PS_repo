import sys
n, k = map(int, sys.stdin.readline().split())
arr = [] 
for i in range(n) :
    arr.append(int(sys.stdin.readline()))
cnt = 0
for i in range(len(arr)-1,-1,-1) :

    if arr[i] > k :
        continue
    else :
        cnt += k // arr[i]
        k = k % arr[i]
    if k == 0 :
        print(cnt)
        break