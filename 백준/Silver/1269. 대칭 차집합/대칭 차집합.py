import sys

n, m = map(int,sys.stdin.readline().split())

a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))

A, B = dict(), dict()

for i in range(len(a)) :
    if a[i] not in A :
        A[a[i]] = i
for i in range(len(b)) :
    if b[i] not in B :
        B[b[i]] = i

A_cnt, B_cnt = 0, 0
for k,v in A.items() :
    if k not in B :
        A_cnt += 1

for k,v in B.items() :
    if k not in A :
        B_cnt += 1
print(A_cnt+B_cnt)