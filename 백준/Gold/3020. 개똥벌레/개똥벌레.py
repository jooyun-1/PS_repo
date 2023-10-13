import sys

N, H = map(int,sys.stdin.readline().split())
up = [0] * (H+1) # 석순
down = [0] * (H+1) # 종유석
for n in range(1,N+1) :
    size = int(sys.stdin.readline())
    if n % 2 == 1 : # 석순 높이 배열에 입력
        up[size] += 1
    else : # 종유석 높이 배열에 입력
        down[size] += 1
for i in range(H-1,0,-1) :
    up[i] += up[i+1] # 석순 합 누적
    down[i] += down[i+1] # 종유석석  누적
cnt = n
same_range = 1
for i in range(1,H+1) :
    if cnt > up[i] + down[H-i+1] : # 장애물의 개수가 최소일 시,
        cnt = up[i] + down[H-i+1] # 최소 개수 갱신
        same_range = 1 # 구간도 갱신
    elif cnt == (up[i] + down[H-i+1]): # 최소 개수 일치하면,
        same_range += 1 # 구간 + 1
print(cnt, same_range)