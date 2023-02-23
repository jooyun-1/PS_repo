# 금민수 : 4와 7로만 이루어진 수
import sys
A,B = map(int,input().split())
Q = [4,7]
ans = 0
while Q:
    F = Q[0]
    Q.pop(0)

    if F <= B:
        if A<=F:
            ans +=1
        Q.append(F*10+4)
        Q.append(F*10+7)

print(ans)
#a, b = map(int,sys.stdin.readline().split())

# cnt = 0
# flag = True
# for i in range(a, b+1) :
#     s = str(i)
#     if '4' not in s or '7' not in s :
#         continue
#     if s.count('4') + s.count('7') == len(s) :
#         cnt += 1   
    # for j in range(len(s)) :
    #     if s[j] == '4' or s[j] == '7': 
    #         flag =  True
    #     else :
    #         flag = False
    #         break
    # if flag == True :
    #     cnt += 1   
# print(cnt)
