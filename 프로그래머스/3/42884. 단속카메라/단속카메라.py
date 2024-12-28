def solution(routes):
    answer = 1
    routes = list(sorted(routes,key = lambda x : x[1]))
    r1, r2 = routes[0][0], routes[0][1]
    for i in range(1,len(routes)) :
        start, end = routes[i][0], routes[i][1]
        if start > r2 :
            answer += 1
            r2 = end
        
    return answer