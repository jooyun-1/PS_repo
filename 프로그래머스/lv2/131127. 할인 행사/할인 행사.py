from collections import defaultdict
def solution(want, number, discount):
    answer = 0
    goods = dict()
    discount_goods  = defaultdict(int)
    cnt = 0
    for i in range(len(want)) :
        goods[want[i]] = number[i]
    for i in range(len(discount)-9) :
        discount_goods = defaultdict(int)
        cnt += 1
        for j in range(i,i+10) :
            discount_goods[discount[j]] += 1
        flag = True
        for k in range(len(want)) :
            if discount_goods[want[k]] != number[k] :
                flag = False
                break
        if flag == True :
            answer += 1

    return answer