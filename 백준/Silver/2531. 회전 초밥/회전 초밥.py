# 한 위치부터 k개의 접시를 연속해서 먹으면 할인된 가격
# 종류 하나가 쓰인 쿠폰 발행
# => 1번 행사에 참가하면, 쿠폰초밥 하나 무료 제공
# 없으면 새로 만듬
import sys

n, d, k, c = map(int, sys.stdin.readline().split())

arr = []
possible = []
for i in range(n) :
    arr.append(int(sys.stdin.readline()))
for i in range(k) :
    arr.append(arr[i])

for i in range(n) :
    temp = []
    for j in range(i,i+k) :
        temp.append(arr[j])
    possible.append(list(set(temp)))
    # for j in range(i,i+k) :
    #     if arr[j] not in temp :
    #         temp.append(arr[j])
    #     else :
    #         break
    # if len(temp) == k :
    #     possible.append(temp)
answer = 0
for a in range(len(possible)) :
    cnt = len(possible[a])
    if c not in possible[a] :
        cnt += 1
    answer = max(answer, cnt) 
print(answer)