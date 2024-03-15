from itertools import combinations

def solution(orders, course):
    set_menu = dict()
    answer = []
    for c in course :
        for ord in orders :
            for combi in combinations(ord,c) :
                combi = sorted(combi)
                combi = ''.join(combi)
                if combi not in set_menu :
                    set_menu[combi] = 0
                set_menu[combi] += 1
    set_menu = {foods : cnt for foods,cnt in set_menu.items() if cnt > 1}
    set_menu = sorted(set_menu.items(), key = lambda x : (len(x[0]), -x[1]))
    menu_cnt = dict(zip(course,[-1] * len(course)))
    for food, cnt in set_menu :
        if menu_cnt[len(food)] <= cnt :
            menu_cnt[len(food)] = cnt
            answer.append(food)
        
    return sorted(answer)