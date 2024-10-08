N = int(input())
arr = list(map(int,input().split()))
arr.sort()

answer = []
left, right = 0, N-1
res = abs(arr[left] + arr[right])
final = [arr[left], arr[right]]

while left < right :
    temp = arr[left] + arr[right]
    if abs(temp) < res :
        res = abs(temp)
        final = [arr[left], arr[right]]


    if temp < 0 :
        left += 1
    else :
        right -= 1

print(final[0], final[1])