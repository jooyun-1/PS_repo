def change(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1] 
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력

def isPrime(arr) :
    cnt = 0
    for i in range(len(arr)) :
        n = int(arr[i])

        flag = True
        for j in range(2,int(n**(1/2))+1) :
            # print(n,n%j)
            if n % j == 0 :
                flag = False
                break
        if flag and n != 1 :
            cnt += 1
    return cnt
def solution(n, k):
    answer = -1
    result = change(n,k)
    temp = []
    arr = []
    for c in result :
        if c != '0' :
            temp.append(c)
        else :
            if temp :
                arr.append(''.join(temp))
                temp = []
    if temp :
        if '0' not in temp :
            arr.append(''.join(temp))
    # print(arr,result)
    answer = isPrime(arr)
    return answer