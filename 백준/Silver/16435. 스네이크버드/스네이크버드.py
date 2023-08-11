# 과일 하나 먹으면 길이 1 늘어남
# i번째 과일 높이 h
# 자신의 길이보다 작거나 같은 높이 => 먹을 수 있음

N, L = map(int,input().split())

fruits = list(map(int,input().split()))
fruits.sort()
for f in fruits :
    if f <= L :
        L += 1
print(L)