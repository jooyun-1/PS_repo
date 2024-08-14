import sys

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
answer = [0] * n

for i in range(n) :
    cnt = 0
    for j in range(n) :
        if answer[j] == 0 and cnt == arr[i] :
            answer[j] = i + 1
            break
        elif answer[j] == 0 :
            cnt += 1
print(' '.join(map(str, answer)))