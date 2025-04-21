from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    w = 0
    
    while len(trucks) :
        w -= bridge.popleft()
        if w + trucks[0] <= weight :
            bridge.append(trucks[0])
            w += trucks.popleft()
        else :
            bridge.append(0)
        answer += 1
    answer += len(bridge)
    return answer