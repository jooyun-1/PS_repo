def solution(a, b, n):
    answer = 0

    while n >= a :
            bottles_cnt = n // a*b
            remainder = n % a

            answer += bottles_cnt
            n = bottles_cnt + remainder 
    return answer