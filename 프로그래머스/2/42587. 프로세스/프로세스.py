def solution(priorities, location):
    answer = 1
    index = location
    while len(priorities) :
        maxVal = max(priorities)
        if index < 0 :
            index = len(priorities) - 1
        else :
            p = priorities.pop(0)
            if p < maxVal :
                priorities.append(p)
                index -= 1
            else :
                if index == 0 :
                    return answer
                else :
                    index -= 1
                    answer += 1
    return answer