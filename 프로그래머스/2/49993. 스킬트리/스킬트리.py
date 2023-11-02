import copy
def solution(skill, skill_trees):
    answer = 0

    for st in skill_trees :
        copy_skill = list(copy.deepcopy(skill))
        flag = True
        for i in range(len(st)) :
            # if len(copy_skill) > 0 :
            if st[i] in copy_skill :
                if st[i] == copy_skill[0] :
                    copy_skill.pop(0)
                    print(st,copy_skill)
                    if len(copy_skill) == 0 :
                        print(st)
                        break
                else :
                    flag = False
                    break
        if flag == True :
            answer += 1
    return answer