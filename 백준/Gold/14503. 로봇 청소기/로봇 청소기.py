# 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸 청소
# 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈칸 x => 바라보는 방향을 유지한채 한칸 후진 후, 1번으로 돌아감
# 2-1) 후진 못하면, 작동 멈춤
# 3. 현재 칸의 주변 4칸 중 청소 안 된 빈칸이 있는 경우
# 3-1) 반시계 방향으로 90도 회전
# 3-2) 바라보는 방향을 기준을 앞쪽 칸이 청소되지 않은 빈칸인 경우 => 한 칸 전진
# 3-3) 1번으로 돌아감
# 0 : 북, 1 : 동, 2 : 남, 3 : 서
import sys

N, M = map(int,sys.stdin.readline().split())
r, c, d = map(int,sys.stdin.readline().split()) # 첫 로봇 좌표, 바라보는 방향
room = []
for n in range(N) :
    line = list(map(int,sys.stdin.readline().split()))
    room.append(line)
visited = [[0] * M for _ in range(N)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
cnt = 1
visited[r][c] = 1
while True :
    flag = False
    for i in range(4) :
        d = (d+3) % 4
        nx = r + dx[d]
        ny = c + dy[d]

        if 0 <= nx < N and 0 <= ny < M and room[nx][ny] == 0:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                flag = True
                cnt += 1
                r = nx
                c = ny
                break
    if flag == False :
        if room[r - dx[d]][c - dy[d]] == 1 :
            print(cnt)
            break
        else :
            r = r - dx[d]
            c = c - dy[d]