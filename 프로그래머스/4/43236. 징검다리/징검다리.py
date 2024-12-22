def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)
    left, right = 1, distance
    delete = 0
    prev_rock = 0
    while left <= right :
        mid = (left + right) // 2
        delete = 0
        prev_rock = 0
        for rock in rocks :
            diff = rock - prev_rock
            if diff < mid :
                delete += 1
                if delete > n :
                    break
            else :
                prev_rock = rock
        if delete > n :
            right = mid - 1
        else :
            answer = mid
            left = mid + 1
    return answer