def solution(routes):
    answer = 0
    cur = -30000
    routes.sort(key=lambda x : x[1])
    
    for route in routes :
        if route[0] > cur :
            answer += 1
            cur = route[1]
    return answer