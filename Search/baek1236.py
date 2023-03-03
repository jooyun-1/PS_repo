# 직사각형의 성, 1층 = 몇 명의 경비원
# 모든 행과 열에 한명 이상의 경비원
# 행, 열 검사 이중 for? 브루트 포스식?
import sys
N, M = map(int,sys.stdin.readline().split())
# N : 세로 길이, M : 가로 길이
castle = [[0] * M for _ in range(N)]

cnt,cnt2 = 0, 0
for i in range(N) :
    line = sys.stdin.readline()
    for j in range(M) :
        castle[i][j] = line[j]

for i in range(N) :
    if 'X' not in castle[i] :
        cnt += 1
for j in range(M) :
    if 'X' not in [castle[i][j] for i in range(N)] :
        cnt2 += 1
print(max(cnt,cnt2))    