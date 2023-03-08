# 뒤의 트로피가 앞의 트로피에 가려져 있다
N = int(input())
height = []
for i in range(N) :
    h = int(input())
    height.append(h)
left = []
right = []
maxVal = 0
for h in height:
    if maxVal == h :
        continue
    maxVal = max(h,maxVal)
    if maxVal == h :
        left.append(h)
height.reverse()
maxVal = 0
for h in height:
    if maxVal == h :
        continue
    maxVal = max(h,maxVal)
    if maxVal == h :
        right.append(h)
print(len(left))
print(len(right))
