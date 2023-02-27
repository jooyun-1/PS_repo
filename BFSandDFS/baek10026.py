# R, G, B
# 같은 색상이 상하좌우 인접 => 구역
import sys
sys.setrecursionlimit(100000)

N = int(sys.stdin.readline())
grid = [[] for i in range(N)]
visited = [[0]*N for i in range(N)]
diff_cnt, cnt = 0 , 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(N) :
    line = input()
    for j in range(len(line)) :
        grid[i].append(line[j])

def dfs(x, y) :
    global flag
    if x >=N or x < 0 or y >=N or y < 0 :
        return
    
    if flag == grid[x][y] and visited[x][y] == 0 :
        
        visited[x][y] = 1
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)

for i in range(N) :
    for j in range(N) :
        flag = grid[i][j]
        if visited [i][j] == 0 :
            diff_cnt += 1                   
            dfs(i,j)


for i in range(N) :
    for j in range(N) :
       if grid[i][j] == 'R' :
        grid[i][j] = 'G'
visited = [[0]*N for i in range(N)]
for i in range(N) :
    for j in range(N) :
        flag = grid[i][j]
        if visited [i][j] == 0 :
            cnt += 1                   
            dfs(i,j)
print(diff_cnt,cnt)
