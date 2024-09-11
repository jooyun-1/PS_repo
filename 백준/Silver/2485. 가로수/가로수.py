import sys

n = int(sys.stdin.readline())
arr, sub = [], []
answer = 0

for i in range(n) :
    arr.append(int(sys.stdin.readline()))
arr.sort()
for i in range(len(arr)-1) :
    sub.append(arr[i+1]-arr[i])

def f_gcd(a,b) :
    while b > 0 :
        a, b = b, a % b
    return a

gcd = sub[0]
for i in range(1,len(sub)) :
    gcd = f_gcd(gcd,sub[i])

for s in sub :
    answer += s // gcd - 1
print(answer)