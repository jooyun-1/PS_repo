n = int(input())

numbers = list(map(int,input().split()))
numbers.sort()
x = int(input())
left, right = 0, n-1
answer = 0

while left < right :
    temp = numbers[left] + numbers[right]
    if temp == x :
        answer += 1
        left += 1
    elif temp < x :
        left += 1
    else :
        right -= 1
print(answer)