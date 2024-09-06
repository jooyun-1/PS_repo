import sys

n = int(sys.stdin.readline())
arr = set()
for i in range(n) :
    s = sys.stdin.readline().rstrip()
    arr.add(s)
arr =list(arr)
arr.sort(key=lambda x : (len(x),x))

for a in arr :
    print(a)