def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)
    left, right = 1, distance

    while left <= right :
        mid = (left + right) // 2
        prev = 0
        delete = 0
        for rock in rocks :
            dist = rock - prev
            if dist < mid :
                delete += 1
            else :
                prev = rock
        if delete > n :
            right = mid - 1
        else :
            answer = mid
            left = mid + 1
    return answer