N, C = map(int,input().split())
arr = []
for i in range(N) :
    x = int(input())
    arr.append(x)
arr.sort()
start, end = 1, arr[-1] - arr[0]
answer = 0

while start <= end :
    mid = (start + end) // 2
    cnt, cur = 1, arr[0]
    for i in range(1,len(arr)) :
        if arr[i] >= cur + mid :
            cnt += 1
            cur = arr[i]
    if cnt >= C :
        start = mid + 1
        answer = mid
    else :
        end = mid - 1
print(answer)