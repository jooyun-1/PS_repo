# n개의 트럭, 순서는 바꿀 수 없다, 무게는 다를 수 있다
# 다리 위에는 w대의 트럭만 동시에 가능
# 동시 트럭들 무게 합 <= 다리의 최대하중(L)
# 다리의 길이 : w 단위길이, 각 트럭은 하나의 단위시간 내에 하나의 단위 길이만큼만 이동
import sys
n, w, L = map(int,sys.stdin.readline().split()) # n: 트럭 수, w: 다리의 길이, L: 최대 하중
trucks = list(map(int,sys.stdin.readline().split()))
bridge = list()
total,time = 0, 0

while True :
    if len(trucks) == 0 and total == 0 :
        break
    if len(bridge) == w :
        truck = bridge.pop(0)
        total -= truck
    if len(trucks) > 0 and total + trucks[0] <= L :
        bridge.append(trucks[0])
        total += trucks[0]
        trucks.pop(0)
    else :
        bridge.append(0)
    time += 1
print(time)