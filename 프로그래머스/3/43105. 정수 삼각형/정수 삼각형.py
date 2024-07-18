def solution(triangle):
    answer = 0
    floors = len(triangle) - 1
    
    while floors > 0 :
        for i in range(floors) :
            triangle[floors-1][i] += max(triangle[floors][i], triangle[floors][i+1])
        floors -= 1
    answer = triangle[0][0]
    return answer