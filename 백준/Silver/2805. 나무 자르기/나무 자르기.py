N, M = map(int,input().split())
heights = list(map(int,input().split()))

heights.sort()
start, end = 1, heights[-1]
answer = 0
while start <= end :
    mid = (start + end) // 2
    temp = 0
    for h in heights :
        if h > mid :
            temp += (h - mid)
    if temp < M :
        end = mid - 1
    else :
        answer = mid
        start = mid + 1
print(answer)