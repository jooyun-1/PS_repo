# 15번 팔씨름 => 8번 이상 이기면 면제
# S[i] == 'o' : 소정 승

t = int(input())

for test in range(1,t+1) :
    s = input().rstrip()
    cnt_o = 0
    cnt_x = 0
    for i in range(len(s)) :
        if s[i] == 'o' :
            cnt_o += 1
        else :
            cnt_x += 1

    if cnt_x <= 7 :
        answer = 'YES'
    else :
        answer = 'NO'
    print('#{} {}'.format(test,answer))