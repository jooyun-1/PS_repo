# 덧, 뺄, 곱, 나 순서 (입력)
from itertools import permutations
N = int(input())
nums = list(map(int,input().rstrip().split()))
line = list(map(int,input().rstrip().split()))
operators = ['+', '-', '*', '//']
arr = []
for i in range(len(line)) :
    for j in range(line[i]) :
        arr.append(operators[i])
permu = list(permutations(arr,len(arr)))
max_sum, min_sum = float('-inf'), float('inf')
for per in permu :
    sum = nums[0]
    for i in range(len(per)) :
        if per[i] == '+' :
            sum += nums[i+1]
        elif per[i] == '-' :
            sum -= nums[i+1]
        elif per[i] == '//' :
            if sum < 0 :
                sum = (abs(sum) // nums[i+1]) * -1
            else :
                sum = sum // nums[i+1]
        elif per[i] == '*' :
            sum = sum * nums[i + 1]
    max_sum = max(sum,max_sum)
    min_sum = min(sum,min_sum)
print(max_sum)
print(min_sum)