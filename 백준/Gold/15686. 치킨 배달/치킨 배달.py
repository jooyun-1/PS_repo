import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
city = []
home = []
chicken = []
answer = float('inf')

for n in range(N) :
    line = list(map(int,sys.stdin.readline().split()))
    city.append(line)
for i in range(N) :
    for j in range(N) :
        if city[i][j] == 1 :
            home.append([i,j])
        elif city[i][j] == 2:
            chicken.append([i,j])

for chick in combinations(chicken, M) :
    total = 0
    for h in home :
        dist = float('inf')
        for c in chick :
            dist = min(dist, abs(h[0] - c[0]) + abs(h[1] - c[1]))
        total += dist
    answer = min(answer,total)
print(answer)