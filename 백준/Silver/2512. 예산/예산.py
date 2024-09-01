import sys

n = int(sys.stdin.readline())

arr = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
answer = 0
left, right = 0, max(arr)
while left <= right :
    mid = (left + right) // 2
    total = 0
    for i in range(len(arr)) :
        if mid >= arr[i] :
            total += arr[i]
        else :
            total += mid
    if total <= m :
        answer = mid
        left = mid + 1
    else :
        right = mid - 1
print(answer)