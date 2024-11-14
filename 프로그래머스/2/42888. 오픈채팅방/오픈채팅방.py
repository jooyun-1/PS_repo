def solution(record):
    answer = []
    dic = dict()
    for rec in record :
        parts = rec.split()
        if parts[0] != 'Leave' :
            command, uid, name = parts[0], parts[1], parts[2]
            dic[uid] = name

    for rec in record :
        parts = rec.split()
        if parts[0] == 'Enter' :
            answer.append(dic[parts[1]] + "님이 들어왔습니다.")
        elif parts[0] == 'Leave' :
            answer.append(dic[parts[1]] + "님이 나갔습니다.")        
            
    return answer