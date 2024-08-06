import sys
n = int(sys.stdin.readline()) # 지방의 수
moneys = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
answer = 0
left, right = 0, max(moneys)
while left <= right :
    mid = (left + right) // 2
    total = 0
    for i in range(n) :
        if moneys[i] > mid :
            total += mid
        else :
            total += moneys[i]
    if total <= m :
        answer = mid
        left = mid + 1
    else :
        right = mid - 1
print(answer)
