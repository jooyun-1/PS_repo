# 한 점에서 다른 한 점
# 그려진 선들의 총 길이
import sys
N = int(sys.stdin.readline())
ruler = []
dist = 0
for i in range(N) :
    x, y = map(int, sys.stdin.readline().split())
    ruler.append((x,y))
ruler = list(sorted(ruler, key = lambda x : x[0]))

minVal = ruler[0][0]
maxVal = ruler[0][1]
dist = (maxVal - minVal)
for i in range(1,len(ruler)) :
    end = ruler[i][1]
    minVal = max(maxVal, ruler[i][0])
    if end < minVal :
        continue
    maxVal = end
    dist += (maxVal - minVal)
print(dist)