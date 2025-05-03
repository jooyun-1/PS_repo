import sys

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

left, right = 0, 0
answer = 1e9
total = 0

while True :

    if total >= S :
        answer = min(answer,right - left)
        temp = arr[left]
        total -= temp
        left += 1
    elif right == N :
        break
    else :
        total += arr[right]
        right += 1
if answer == 1e9 :
    print(0)
else:
    print(answer)