def gcd(a,b) :
    while b > 0 :
        a, b = b, a % b
    return a
        
def solution(arrayA, arrayB):
    answer = 0
    gcd_a = arrayA[0]
    gcd_b = arrayB[0]
    flagA = True
    flagB = True
    
    for i in arrayA[1:] :
        gcd_a = gcd(i,gcd_a)
    for j in arrayB[1:] :
        gcd_b = gcd(j,gcd_b)
    
    for i in arrayB :
        if i % gcd_a == 0 :
            flagA = False
            break
    if flagA :
        answer = max(answer,gcd_a)
        
    for j in arrayA :
        if j % gcd_b == 0 :
            flagB = False
            break
    if flagB :
        answer = max(answer,gcd_b)
    
    return answer