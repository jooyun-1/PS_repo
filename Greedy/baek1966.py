# 현재 큐의 가장 앞에 있는 문서의 중요도 확인
# 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있으면 인쇄X
# 그 후, 큐의 가장 뒤에 배치
# 아니면 그냥 인쇄
T = int(input()) # 테스트케이스의 수
for i in range(T):
    N,M = map(int,input().split()) # N: 문서의 개수, M: 큐에서 몇번째 놓여져있는지
    que = list(map(int,input().split())) # 각 문서의 중요도 입력
    cnt = 0
    while M != -1 : # M이 -1이 되었을 때 빠져나옴
        if que[0] == max(que) : 
            del que[0]
            cnt += 1
            M -= 1
        else :
            que.append(que[0])
            del que[0]
            if M == 0 : # M이 0인데도 max가 아니므로 뒤로 보내야됨
                M = len(que) - 1
            else :
                M -= 1
    print(cnt)
        

