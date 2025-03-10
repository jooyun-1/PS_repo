def solution(gems):
    answer = [0,len(gems)]
    left, right = 0, 0
    gems_dict = {gems[0] : 1}
    size = len(set(gems))
    
    while left < len(gems) and right < len(gems) :
        if len(gems_dict) == size :
            if right - left < answer[1] - answer[0] :
                answer = [left, right]
            else :
                gems_dict[gems[left]] -= 1
                if gems_dict[gems[left]] == 0 :
                    del gems_dict[gems[left]]
                left += 1
        else :
            right += 1
            if right == len(gems):
                break
            if gems[right] in gems_dict :
                gems_dict[gems[right]] += 1
            else :
                gems_dict[gems[right]] = 1            
    return [answer[0]+1, answer[1]+1]