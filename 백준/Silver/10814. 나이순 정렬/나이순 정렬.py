import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n) :
    age, name = sys.stdin.readline().rstrip().split()
    age = int(age)
    arr.append((i,age,name))
arr.sort(key=lambda x : (x[1],x[0]))

for a in arr :
    print(a[1], a[2])