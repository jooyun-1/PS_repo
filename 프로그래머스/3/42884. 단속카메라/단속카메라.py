def solution(routes):
    answer = 0
    routes.sort(key = lambda x : x[1])
    temp = []
    for r in routes :
        if len(temp) == 0 :
            temp.append(r[1])
        elif r[0] <= temp[-1] <= r[1] :
            continue
        else :
            temp.append(r[1])

    return len(temp)