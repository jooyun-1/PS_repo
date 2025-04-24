def solution(routes):
    answer = 1
    routes = list(sorted(routes,key = lambda x : x[1]))
    now = routes[0][1]
    for i in range(1,len(routes)) :
        start, end = routes[i][0], routes[i][1]
        if now < start :
            now = end
            answer += 1
    return answer