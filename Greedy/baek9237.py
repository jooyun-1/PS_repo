import sys
N = int(sys.stdin.readline())

arr, temp = [], []

arr = list(map(int,sys.stdin.readline().split()))
arr.sort(reverse=True)
for i in range(1,len(arr)+1) :
    temp.append(i+arr[i-1])
print(max(temp) + 1)