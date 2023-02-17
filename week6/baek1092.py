# 크레인 수 : N, 1분에 박스 1개
# 모든 박스를 배로 옮기는 데 드는 최소 시간?
import sys
N = int(input())
crain = list(map(int, input().split()))
M = int(input())
box = list(map(int, input().split()))
box.sort(reverse=True)
crain.sort(reverse=True)
pos = [0] * N # 크레인 현재 위치
visited = [0] * M # 옮겨진 박스
cnt, time = 0, 0

if max(crain) < max(box) :
    print(-1)
    sys.exit()
    
while True :
    if cnt == len(box) :
        break
    for i in range(len(crain)) :
        while pos[i] < len(box) :
            if crain[i] >= box[pos[i]] and visited[pos[i]] == 0 :
                cnt += 1
                visited[pos[i]] = 1
                pos[i] += 1
                break
            pos[i] += 1
    time += 1

print(time)