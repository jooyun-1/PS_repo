import math
t = int(input())

def prime(x) :
    for i in range(2, int(math.sqrt(x))) :
        if x % i == 0 :
            return True
    return False

for test_case in range(t) :
    n = int(input())
    for i in range(n, 10**9+1) :
        if prime(i) and prime(i-n) :
            print("#{} {} {}".format(test_case, i, i-n))
            break
        