# N개의 센서, 최대 K 개의 집중국 세울 수 있음
# 집중국의 수신 가능 영역 : 고속도로 상에서 연결된 구간
# N개의 센서가 적어도 하나의 집중국과는 통신 가능해야 됨
# 각 집중국의 수신 가능 영역의 길이의 합을 최소화해야함
# 센서들은 원점으로부터 정수 거리의 위치
import sys
N = int(sys.stdin.readline()) # 센서의 개수
K = int(sys.stdin.readline()) # 집중국의 개수

if K >= N :
    print(0)
    sys.exit()

sensors = list(map(int,sys.stdin.readline().split()))
sensors.sort() # 센서 좌표 오름차순 정렬
# 3 6 7 8 10 12 14 15 18 20
# 3 1 1 2 2 2 1 3 2 
# 3~6 x 6~7 7~8 8~10 x 10~12 x 12~14 14~15 15~18 x 18~20
# 3 6~8 10 12~15 18~20
distances = []
for i in range(1, N) :
    distances.append(sensors[i] - sensors[i-1]) # 각 센서 사이의 거리 배열
distances.sort(reverse=True)

for i in range(K-1) : # 거리 높은 것 K-1개 끊기! (센서 K개 남도록!)
    distances[i] = 0
print(sum(distances))