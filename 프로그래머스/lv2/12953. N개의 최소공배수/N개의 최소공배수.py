from math import gcd
def solution(arr):
    answer = 1
    answer = arr[0]
    for n in arr :
        answer = (answer * n) // gcd(answer,n)
    # arr = list(set(arr))
    # for i in range(2,max(arr)+1) :
    #     flag = True
    #     for a in arr :
    #         if a % i != 0 :
    #             flag = False
    #             break
    #     if flag == True :
    #         for j in range(len(arr)) :
    #             arr[j] = arr[j] // i
    #         answer *= i
    # for a in arr :
    #     answer *= a
    return answer