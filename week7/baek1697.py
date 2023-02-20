# 수빈 : N, 동생 : K
# 걷기 : X-1, X+1 순간이동 : 2*X
# BFS
# 방문한 정점은 빼주면서 K일 떄까지 탐색

N, K =  map(int, input().split())
Max = 100001 # N, K의 최대 범위
visited = [0] * Max 

def bfs(pos) :
    que = list()
    que.append(pos) # 현재 위치에서 방문할 정점을 que에 담는다
    while que :
        pos = que.pop(0)
        if pos == K :
            print(visited[pos])
            break
        for next_pos in (pos-1, pos+1, pos * 2) :   # 수빈이가 움직일 수 있는 경우의 수마다 방문
            if 0 <= next_pos < Max and visited[next_pos] == 0 : # 다음 위치가 범위 안 and 방문을 안 한 위치일 때
                visited[next_pos] = visited[pos] + 1    # 여태 지난 시간에 +1
                que.append(next_pos)

bfs(N)
