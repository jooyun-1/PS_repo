from collections import deque
def solution(queue1, queue2):
    answer = 0
    deq1 = deque(queue1)
    deq2 = deque(queue2)
    cur1, cur2 = sum(deq1), sum(deq2)
    total = cur1 + cur2
    
    if total % 2 != 0 :
        return -1
        
    while True :
        if cur1 > cur2 :
            num1 = deq1.popleft()
            deq2.append(num1)
            cur1 -= num1
            cur2 += num1
            answer += 1
        elif cur1 < cur2 :
            num2 = deq2.popleft()
            deq1.append(num2)
            cur1 += num2
            cur2 -= num2
            answer += 1 
        else :
            print(answer)
            break
        if answer >= len(queue1) * 4 :
            return -1
    return answer