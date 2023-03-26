import sys
N, K = map(int,sys.stdin.readline().split())
number = sys.stdin.readline().rstrip()
arr = []

for num in number :
    while arr and arr[-1] < num and K > 0:
        arr.pop()
        K -= 1
    arr.append(num)
if K > 0 :
    print(''.join(arr[:-K]))
else :
    print(''.join(arr)) 

# num = []
# maxArr = [0] * N
# diff = [0] * N
# answer = []
# maxVal = float('-inf')
# num = sys.stdin.readline().rstrip()
# for i in range(len(num)-1,-1,-1) :
#     maxVal = max(maxVal,int(num[i]))
#     maxArr[i] = maxVal
#     diff[i] = maxVal - int(num[i])
# for i in range(len(diff)-1,-1,-1) :
#     if len(answer) == (N-K) :
#         break
#     if diff[i] <= diff[i-1] :
#         answer.append(num[i])
#     if i == 0 :
#         if diff[0] <= diff[1] :
#             answer.append(num[0])
# answer.reverse()
# print(int(''.join(answer)))