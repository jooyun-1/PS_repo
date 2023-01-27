def solution(dartResult):
    # 세차례 던져 점수 합계 (각 0~10점)
    # S, D, T = 1 ,2제곱 ,3제곱
    # * => 현 점수와 바로 전 점수 각 2배 , # : 해당 점수 마이너스
    total = []
    n = ''
    for i in dartResult :
        if i.isnumeric() :
            n += i
        elif i == 'S' :
            n = int(n) ** 1
            total.append(n)
            n = ''
        elif i == 'D' :
            n = int(n) ** 2
            total.append(n)
            n = ''
        elif i == 'T' :
            n = int(n) ** 3
            total.append(n)
            n = ''
        elif i == '*' :
            if len(total) > 1 :
                total[-2] *= 2
                total[-1] *= 2
            else :
                total[-1] *= 2
        elif i == '#' :
            total[-1] *= (-1)
    answer = sum(total)
    return answer