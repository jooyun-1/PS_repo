def solution(nums):
    answer = 0
    length = len(set(nums))
    if length > len(nums)/2 :
        answer = len(nums)/2
    else : answer = length
    
    return answer