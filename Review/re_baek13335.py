# 다리 위 w대 트럭
# 다리의 길이 : w
# 트럭 : 하나의 단위시간에 하나의 단위길이
import sys
# 4, 2, 10
n, w, L = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
bridge = []
total, time = 0, 0
while True :
    if len(arr) == 0 and total == 0 :
        break
    if len(bridge) == w :
        truck = bridge.pop(0)
        total -= truck
    if len(arr) > 0 and total + arr[0] <= L :
        bridge.append(arr[0])
        total += arr[0]
        arr.pop(0)
    else :
        bridge.append(0)
    time += 1
print(time)

