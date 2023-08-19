import sys
# X : 유성의 일부, # : 땅의 일부, . : 공기
# 모든 유성 조각은 이어져있음
# 한쪽에서 상하좌우 이동해서 다른 유성 도달 가능 (땅도)

R, S = map(int,sys.stdin.readline().split())
picture = []
answer = [['.'] * S for _ in range(R)]
for r in range(R) :
    line = sys.stdin.readline().rstrip()
    picture.append(line)

diff = float('inf')
for s in range(S) :
    star, land = 0, float('inf')
    flag = False
    for r in range(R) :
        if picture[r][s] == 'X' :
            star = max(star, r)
            flag = True
        if picture[r][s] == '#' :
            land = min(land, r)
    if flag == True :
        diff = min(diff, abs(star - land) - 1)
for r in range(R) :
    for s in range(S) :
        if picture[r][s] == 'X' :
            answer[r + diff][s] = 'X'
        elif picture[r][s] == '#' :
            answer[r][s] = '#'
for i in range(R) :
    for j in range(S) :
        print(answer[i][j],end="")
    print()
