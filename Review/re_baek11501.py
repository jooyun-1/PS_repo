# 주식 하나 산다
# 원하는 만큼 판다
# 아무것도 안한다
import sys
T = int(sys.stdin.readline())
answer = []
for i in range(T) :
    arr = []
    maxVal = 0
    N = int(sys.stdin.readline())
    day = list(map(int,sys.stdin.readline().split()))
    for j in range(len(day)-1,-1,-1) :
        maxVal = max(maxVal,day[j])
        arr.append(maxVal - day[j])
    answer.append(sum(arr))
for ans in answer :
    print(ans)