import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
answer = dict()
sortedArr = list(set(arr))
sortedArr.sort()

for i in range(len(sortedArr)) :
    answer[sortedArr[i]] = i
for i in range(len(arr)) :
    print(answer[arr[i]], end= " ")