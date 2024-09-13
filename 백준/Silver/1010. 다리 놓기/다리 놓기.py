import sys
import math

T = int(sys.stdin.readline())

for i in range(T) :
    n, m = map(int,sys.stdin.readline().split())
    print(math.comb(m,n))
