from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)

    while True :
        if len(people) > 1 :
            if people[0] + people[-1] <= limit :
                people.popleft()
                people.pop()
                answer += 1
            else :
                people.pop()
                answer += 1                
        elif len(people) == 1:
            people.pop()
            answer += 1
        else :
            break
    return answer