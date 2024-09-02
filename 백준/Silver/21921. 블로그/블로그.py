import sys

n, x = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
if max(arr) == 0 :
    print('SAD')
    exit(0)
    
val = sum(arr[:x])
max_val = val
max_cnt = 1

for i in range(x,n) :
    val += arr[i]
    val -= arr[i-x]
    if val > max_val :
        max_val = val
        max_cnt = 1
    elif val == max_val :
        max_cnt += 1
print(max_val)
print(max_cnt)
