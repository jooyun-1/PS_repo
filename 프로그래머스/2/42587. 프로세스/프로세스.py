# 1. 실행 대기 큐(Queue)에서 대기중인 프로세스 하나를 꺼냅니다.
# 2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣습니다.
# if max(priorities) > process : priorities.append(process)
# 3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행합니다.
#  3.1 한 번 실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료됩니다.
from collections import deque

def solution(priorities, location):
    answer = 0
    que = deque(priorities)
    while True :
        if location == -1 :
            location = len(que) - 1
        max_p = max(que)
        process = que.popleft()
        if process == max_p :
            if location == 0 :
                answer += 1
                break
            else :
                location -= 1
        else :
            que.append(process)
            answer -= 1
            location -= 1
        answer += 1
    return answer