import sys

import sys

ans = 4


def solve(cnt, num):
    global ans
    if cnt >= ans:
        return
    if check(): # 출발지점 = 도착지점
        ans = cnt 
        return
    for idx in range(num + 1, len(candidates)): # 후보 Brute forth
        i, j = candidates[idx]
        if lines[i][j - 1] == 0 and lines[i][j + 1] == 0:
            lines[i][j] = 1
            solve(cnt + 1, idx)
            lines[i][j] = 0


def check(): # 출발 지점과 도착 지점 같은지
    for i in range(1, N + 1):
        now = i
        for j in range(1, H + 1):
            if lines[j][now] == 1: # 오른쪽
                now += 1
            elif lines[j][now - 1] == 1: # 왼쪽
                now -= 1
        if i != now:
            return False
    return True


N, M, H = map(int, sys.stdin.readline().split())
lines = [[0 for _ in range(N + 1)] for _ in range(H + 1)]
candidates = []
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    lines[x][y] = 1
for i in range(1, H + 1): # 가로선 놓을 수 있는 후보들 append
    for j in range(1, N):
        if lines[i][j] == 0 and lines[i][j - 1] == 0 and lines[i][j + 1] == 0:
            candidates.append([i, j])
solve(0, -1)
print(ans if ans < 4 else -1)

