import heapq
def solution(operations):
    answer = []
    for s in operations :
        op = s.split(" ")
        if op[0] == 'I' :
            heapq.heappush(answer, int(op[1]))
        elif op[0] == 'D' and op[1] == '1' :
            if len(answer) > 0 :
                answer.pop()
        else :
            if len(answer) > 0 :
                heapq.heappop(answer)

    if len(answer) == 0 :
        answer = [0,0]
    else :
        answer = [max(answer), min(answer)]
    return answer