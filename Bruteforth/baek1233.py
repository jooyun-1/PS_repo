from itertools import combinations
s1, s2, s3 = map(int,input().split())
arr1 = [i for i in range(1,s1+1)]
arr2 = [i for i in range(1,s2+1)]
arr3 = [i for i in range(1,s3+1)]
result = [0] * (len(arr1) + len(arr2) + len(arr3)+1)
sum = 0
for i in range(len(arr1)) :
    for j in range(len(arr2)) :
        for k in range(len(arr3)) :
            sum = arr1[i]+ arr2[j]+arr3[k]            
            result[sum] += 1
print(result.index(max(result)))
