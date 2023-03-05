import sys
N, M = map(int,sys.stdin.readline().split())
graph = []
cnt, cnt2 = 0, 0
for i in range(N) :
    line = sys.stdin.readline()
    graph.append(line)

for n in range(N) :
    if 'X' not in graph[n] :
        cnt += 1
for m in range(M) :    
    if 'X' not in [graph[n][m] for n in range(N)] :
        cnt2 += 1
print(max(cnt, cnt2)) 