import copy
def solution(skill, skill_trees):
    answer = 0
    skill = list(skill)
    for sk in skill_trees :
        temp = copy.deepcopy(skill)
        flag = True
        for i in range(len(sk)) :
            if sk[i] in skill :
                if sk[i] != temp[0] :
                    flag = False
                    break
                else :
                    if len(temp) > 0 :
                        temp.pop(0)
        if flag :
            answer += 1
    return answer