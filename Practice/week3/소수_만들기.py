from itertools import combinations

def isPrime(num):
    for i in range(2, int(num**0.5) + 1) :
        if num % i == 0 :
            return False
    return True

def solution(nums):
    answer = 0
    temp = list(combinations(nums,3))
    for i in range(len(temp)) :
        total = sum(temp[i])
        flag = isPrime(total)
        if flag == True :
            answer+=1
            
    return answer