# 재료 : 각각 고유한 번호 가짐
# 두 개의 재료 = 두 재료의 고유한 번호의 합이 M
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

arr = list(map(int,sys.stdin.readline().split()))

# allList = list(combinations(arr,2))
cnt = 0
arr.sort()
for num in arr :
    if num >= m :
        arr.remove(num)

for i in range(n-1) :
    if arr[i] >= m : 
        break
    for j in range(i+1,n):
        if arr[j] >= m :
            break
        if arr[i] + arr[j] == m :
            cnt += 1

print(cnt)
