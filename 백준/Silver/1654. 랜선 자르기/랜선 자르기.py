K, N = map(int,input().split())
arr = []
for i in range(K) :
    arr.append(int(input()))
arr.sort()
start, end = 1, arr[-1]

while start <= end :
    mid = (start + end) // 2
    lines = 0
    for a in arr :
        lines += a // mid
    if lines >= N :
        start = mid + 1
    else :
        end = mid - 1
print(end)