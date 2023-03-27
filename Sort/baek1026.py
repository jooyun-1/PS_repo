# S의 최솟값
import sys
N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

a = list(sorted(a,reverse=True))
b.sort()
sum = 0
for i in range(N) :
    sum += (a[i] * b[i])
print(sum)