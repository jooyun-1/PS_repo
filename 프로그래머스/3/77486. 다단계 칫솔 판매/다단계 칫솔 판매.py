def solution(enroll, referral, seller, amount):
    answer = []
    money = [0 for _ in range(len(enroll))]
    dic = dict()
    for i, e in enumerate(enroll) :
        dic[e] = i
        
    for s, a in zip(seller,amount) :
        m = a * 100
        while s != '-' and m > 0 :
            idx = dic[s]
            money[idx] += m - m // 10
            m = m // 10
            s = referral[idx]
    return money