def solution(participant, completion):
    answer = []
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    answer = participant[len(participant)-1]        
    return answer