import sys

n = int(sys.stdin.readline())
arr = set()
answer = 0
for i in range(n) :
    s = sys.stdin.readline().rstrip()
    if s == 'ENTER' :
        answer += len(arr)
        arr = set()
    else :
        arr.add(s)
answer += len(arr)
print(answer)
