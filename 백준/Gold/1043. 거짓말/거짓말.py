import sys

n, m = map(int,sys.stdin.readline().split())
parent = [i for i in range(n+1)]
true = list(map(int,sys.stdin.readline().split()))
partys = [list(map(int, input().split())) for _ in range(m)]

def find(x) :
    if parent[x] == x :
        return x
    parent[x] = find(parent[x])
    return parent[x]
def union(a,b) :
    x = find(a)
    y = find(b)
    parent[y] = x

if true[0] == 0:
    print(m)  
    exit()

for i in range(2, len(true)):
    union(true[1], true[i])

for party in partys :
    for i in range(2, len(party)) :
        union(party[1],party[i])

answer = 0
x = find(true[1])

for party in partys :
    if find(party[1]) != x :
        answer += 1
print(answer)