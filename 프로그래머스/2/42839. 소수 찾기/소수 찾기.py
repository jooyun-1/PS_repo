from itertools import permutations
import math

def solution(numbers):
    answer = 0
    arr = list(map(str,numbers))
    temp = set()

    for i in range(1,len(numbers)+1) :
        num = list(permutations(arr,i))
        for n in num :
            temp.add(int(''.join(n)))
    
    nums = list(temp)
    
    for n in nums :
        flag = True
        for i in range(2,int(math.sqrt(n))+1) :
            if n % i == 0 :
                flag = False
                break
        if flag :
            if n >= 2 :
                answer += 1

    return answer