def solution(record):
    answer = []
    nickname = dict()
    for i in range(len(record)) :
        arr = list(record[i].split())
        if arr[0] == 'Enter' or arr[0] == 'Change' :
            nickname[arr[1]] = arr[2]
    
    for i in range(len(record)) :
        arr = list(record[i].split())
        if arr[0] == 'Enter' :
            str = nickname[arr[1]] + "님이 들어왔습니다."
            answer.append(str)
        elif arr[0] == 'Leave' :
            str = nickname[arr[1]] + "님이 나갔습니다."
            answer.append(str)
    return answer