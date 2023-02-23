S = input()
zero_cnt = 0
one_cnt = 0
if S[0] == '0' :
    flag = False
if S[0] == '1' :
     flag = True
for i in range(1, len(S)) :    
    if flag == False :
        if S[i] == '1' :
            flag = True
            zero_cnt += 1
    if flag == True :
        if S[i] == '0' :
            flag = False
            one_cnt += 1
if flag == True :
    one_cnt += 1
if flag == False :
    zero_cnt += 1
print(min(zero_cnt,one_cnt))
    