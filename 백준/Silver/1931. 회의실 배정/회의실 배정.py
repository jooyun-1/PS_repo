import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n) :
    start, end = map(int,sys.stdin.readline().split())
    arr.append([start,end])
arr.sort(key=lambda x : (x[1],x[0]))
answer = 0
cur_start, cur_end = 0, 0
for start,end in arr :
    if cur_end <= start :
        answer += 1
        cur_end = end
print(answer)