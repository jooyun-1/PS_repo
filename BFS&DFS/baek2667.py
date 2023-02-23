# 집 : 1 , 집 없는 곳: 0
# 연결 : 어떤 집이 상하좌우 중 하나에 다른 집이 있는 경우

N = int(input())
graph = [[0] * (N) for i in range(N)]  # 지도 
visited = [[0] * (N) for i in range(N)] # 방문한 집
result = [] # 출력할 결과
dx = [0,0,1,-1] # 행 1칸 이동
dy = [1,-1,0,0] # 열 1칸 이동
cnt = 0

for i in range(N) :
    temp = input()
    for j in range(len(temp)) :
        graph[i][j] = int(temp[j])  # 지도 입력

def dfs(x, y) :
    global cnt
    if x < 0 or x >= N or y < 0 or y >= N : # 행, 열 값이 지도를 넘기면 return
        return
    if visited[x][y] == 0 and graph[x][y] == 1 :  # 방문한 곳이 아니고 1인 곳   
        cnt += 1
        visited[x][y] = 1
        for i in range(4) : # 한 집당 네 방향 이동
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)

for a in range(N) :
    for b in range(N) :
        if graph[a][b] == 1 and visited[a][b] == 0:            
            dfs(a,b)
            result.append(cnt)
            cnt = 0
result.sort()
print(len(result))
for r in result :
    print(r)