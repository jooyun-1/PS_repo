import sys
import math
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
x = list(map(int, input().rstrip().split()))

res = x[0]
for i in range(1, m):
    res = max(res, math.ceil((x[i] - x[i - 1]) / 2))
res = max(res, n - x[-1])

print(res)