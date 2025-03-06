import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
perm = list(set(list(permutations(arr,M))))
perm.sort()
for per in perm :
    for p in per :
        print(p, end = ' ')
    print()
