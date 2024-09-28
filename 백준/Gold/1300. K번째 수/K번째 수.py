N = int(input())
k = int(input())

start, end = 0, k
answer = 0

while start <= end :
    cnt = 0
    mid = (start + end) // 2
    for i in range(1, N+1) :
        cnt += min(N, mid // i)
    if cnt >= k :
        answer = mid
        end = mid - 1
    else :
        start = mid + 1
print(answer)        