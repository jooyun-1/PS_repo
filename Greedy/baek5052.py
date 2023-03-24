# 한 번호가 다른 번호의 접두어인 경우가 없어야 한다
import sys
t = int(sys.stdin.readline())
answer = []
for i in range(t) :
    n = int(sys.stdin.readline())
    phone = []
    for j in range(n) :
        line = sys.stdin.readline().rstrip()
        phone.append(line)
    phone.sort()
    flag = True
    for a in range(len(phone)-1) :
        if phone[a+1][:len(phone[a])] == phone[a] :
        # if phone[a+1].startswith(phone[a]) :
            flag = False
            answer.append("NO")
            break
        #     if phone[a] in phone[a+1] :
        #         flag = False
        #         break
    if flag == True :
        answer.append("YES")
for ans in answer :
    print(ans)
