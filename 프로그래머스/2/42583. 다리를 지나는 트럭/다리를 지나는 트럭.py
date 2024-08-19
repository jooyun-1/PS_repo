from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    w = 0
    while truck_weights:
        w -= bridge.popleft()
        answer += 1
        if w + truck_weights[0] <= weight :
            w += truck_weights[0]
            bridge.append(truck_weights.popleft())
        else :
            bridge.append(0)
    answer += bridge_length
    return answer