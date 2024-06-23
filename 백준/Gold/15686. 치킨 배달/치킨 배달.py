from itertools import combinations
N, M = map(int,input().split())
city = []
home, chicken = [], []
for n in range(N) :
    line = list(map(int,input().split()))
    city.append(line)
for r in range(N) :
    for c in range(N) :
        if city[r][c] == 1 :
            home.append([r,c])
        elif city[r][c] == 2 :
            chicken.append([r,c])
combi = list(combinations(chicken,M))
answer = float('inf')
for com in combi :
    temp = 0
    for h in home :
        dist = float('inf')
        for c in com :
            dist = min(dist, (abs(h[0] - c[0]) + abs(h[1] - c[1])))
        temp += dist
    answer = min(answer,temp)
print(answer)