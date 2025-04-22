from itertools import permutations

def solution(numbers):
    answer = 0
    arr = list(map(str,numbers))
    nums = set()

    for i in range(1,len(numbers)+1) :
        num = list(permutations(arr,i))
        for n in num :
            nums.add(int(''.join(n)))
    a = []
    for n in nums :
        flag = True
        print(n)
        if n== 0 or n == 1 :
            continue
        for i in range(2, int(n**0.5)+1) :
            if n % i == 0 :
                flag = False
                break
        if flag :
            a.append(n)
            answer += 1
    
    return answer