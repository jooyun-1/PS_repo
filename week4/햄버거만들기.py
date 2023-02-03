# 재료 조리된 순서대로 아래서부터 위로 쌓임
# 순서에 맞게 쌓여 완성된 햄버거를 따로 옮겨 포장
# 빵-야채-고기-빵으로 쌓인 것만 포장
# 1,2,3,1
def solution(ingredient):
    cnt = 0
    temp = []
    for i in ingredient :
        temp.append(i)
        if temp[-4:] == [1,2,3,1]:
            cnt += 1
            for _ in range(4):
                temp.pop()                  
    return cnt