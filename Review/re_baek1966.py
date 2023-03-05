 # 현재 큐의 가장 앞에 있는 문서의 중요도 확인
# 현재 문서보다 중요도 높은 문서 있다면 문서 인쇄 X
# 큐의 가장 뒤에 재배치
import sys
T = int(sys.stdin.readline())
answer = []
for i in range(T) :
    N, M = map(int,sys.stdin.readline().split())
    priority = []
    priority = list(map(int,sys.stdin.readline().split()))
    target = priority[M]
    max_pr = max(priority)
    cnt = 0
    while M != -1 :
        if priority[0] == max(priority) :
            del priority[0]
            M -= 1
            cnt += 1
        else :
            priority.append(priority[0])
            del priority[0]
            if M == 0 :
                M = len(priority) - 1
            else :
                M -= 1
    answer.append(cnt)
for ans in answer :
    print(ans)


