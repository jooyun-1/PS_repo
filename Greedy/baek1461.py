# 세준 현재 위치 0, 마구 놓은 책 0
# 모두 제자리에 놔둘 때 드는 최소 걸음 수
# 한 걸음에 좌표 1칸씩, 한 번에 최대 M권이 책
import sys
N, M = map(int,sys.stdin.readline().split())
books = list(map(int,sys.stdin.readline().split()))
books.sort()
left, right = [], []
sum = 0
for b in books :
    if b < 0 :
        left.append(b)
    elif b > 0 :
        right.append(b)

if len(left) ==0 :
    left.append(0)
elif len(right) == 0:
    right.append(0)

if abs(min(left)) > max(right) :
    sum += abs(left[0])
    for i in range(M,len(left),M) :
        sum += abs(left[i] * 2)
    for i in range(len(right)-1, -1, -M) :
        sum += (right[i] * 2)
elif abs(min(left)) < max(right) :
    sum += right[len(right)-1]
    for i in range(0,len(left),M) :
        sum += abs(left[i] * 2)
    for i in range(len(right)-1-M, -1, -M) :
        sum += (right[i] * 2)

print(sum)
# [-39, -37, -29, -28, -6, 2, 11]
# 0 2 11 0 -6 0 -29 0 -39
# 0 2 -6 0 11 0  
# (-39, -37), (-29, -28), (-6,0), (0, 11)
# [-1, 3, 4, 5, 6, 11]
# 0 -1 3 0 5 0 11
# 0 -1 0 3 0
# (-1,0), (0,3) (4,5) (6,11)
# [-45, -26, -18, -9, -4, 22, 40, 50]
# (-45, -26, -18) , (-9, -4) (22, 40, 50)
