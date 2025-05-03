import sys

N, M = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
total, answer = 0, 0
left, right = 0, 1

while right <= N and left <= right :
    total = sum(arr[left:right])
    if total == M :
        answer += 1
        right += 1
    elif total < M :
        right += 1
    else :
        left += 1
print(answer)