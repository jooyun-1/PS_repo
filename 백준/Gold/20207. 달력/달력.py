N = int(input())
arr = [0] * 366

for n in range(N) :
    start, end = map(int,input().split())
    while start <= end :
        arr[start] += 1
        start += 1

w, h = 0, 0
answer = 0
for i in range(1,366) :
    if arr[i] == 0 :
        answer += w*h
        w,h = 0, 0
    else :
        w += 1
        h = max(h,arr[i])
print(answer + w*h)