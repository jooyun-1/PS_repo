def solution(priorities, location):
    answer = 1
    
    index = location
    while len(priorities) > 1 :
        prior = max(priorities)
        if index < 0 :
            index = len(priorities) - 1
        p = priorities.pop(0)
        if p < prior :
            priorities.append(p)
            index -= 1
        else :
            if index == 0 :
                return answer
            else :
                index -= 1
                answer += 1                
    return answer