import sys

n, m = map(int,sys.stdin.readline().split())

arr1, arr2 = dict(), []
answer = []
for i in range(n) :
    s = sys.stdin.readline().rstrip()
    if s not in arr1 :
        arr1[s] = i
for i in range(m) :
    s = sys.stdin.readline().rstrip()
    if s in arr1 :
        answer.append(s)
answer.sort()
print(len(answer))
for i in range(len(answer)) :
    print(answer[i])
