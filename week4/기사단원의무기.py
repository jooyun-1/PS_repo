# 무기 공격력 = 약수의 개수
# 공격력 1당 철 1kg
# 공격력 제한치 초과하면 => 공격력 정해져있음
def solution(number, limit, power):
    answer = 0
    for i in range(1, number+1):
        cnt = 0
        for j in range(1, int(i**0.5)+1):
            if i % j == 0:
                cnt += 1
                if int(j**2) != i:
                    cnt += 1
        if cnt > limit:
            answer += power
        else :
            answer += cnt
    return answer