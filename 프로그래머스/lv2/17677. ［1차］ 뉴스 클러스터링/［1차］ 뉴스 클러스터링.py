def makeSet(s,arr) :
    for i in range(len(s)) :
        flag = True
        if len(s[i:i+2]) == 2 :
            for c in s[i:i+2] :
                if not c.isalpha() :
                    flag = False
                    break
            if flag == True :
                arr.append(s[i:i+2])
def solution(str1, str2):
    answer = 0
    result = 0
    A, B = [], []
    str1 = str1.upper()
    str2 = str2.upper()
    makeSet(str1,A)
    makeSet(str2,B)
    arr, arr2 = [], []
    prev = []
    for i in range(len(A)) :
        if A[i] in prev :
            continue
        if A[i] in B :
            cnt = min(A.count(A[i]),B.count(A[i]))
            for j in range(cnt) :
                arr.append(A[i])
            prev.append(A[i])
    for i in range(len(A)) :
        B.append(A[i])
    for j in arr :
        B.remove(j)
    if len(A) == 0 and len(B) == 0 :
        result = 1
    else :
        result = len(arr) / len(B)
    print(arr,B)
    return int(result * 65536)