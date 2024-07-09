def solution(routes):
    answer = 0
    routes.sort(key = lambda x : x[1])
    temp = -30001
    
    for route in routes :
        if route[0] > temp :
            answer += 1
            temp = route[1]
    return answer