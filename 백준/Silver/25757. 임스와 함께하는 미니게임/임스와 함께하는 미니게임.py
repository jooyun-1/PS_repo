import sys

N, type = sys.stdin.readline().split()
N = int(N)
arr = set()

for i in range(N) :
    name = sys.stdin.readline().rstrip()
    arr.add(name)
if type == 'Y' :
    print(len(arr))
elif type == 'F' :
    print(len(arr)//2)
elif type == 'O' :
    print(len(arr)//3)