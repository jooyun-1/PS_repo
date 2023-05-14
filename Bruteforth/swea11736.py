t = int(input())

for test in range(1,t+1) :
    n = int(input())
    cnt = 0
    arr = list(map(int,input().split()))
    for i in range(1,len(arr)-1):
        if arr[i] != max(arr[i],arr[i-1],arr[i+1]) and arr[i] != min(arr[i],arr[i-1],arr[i+1]):
            cnt += 1
    print('#{} {}'.format(test,cnt))