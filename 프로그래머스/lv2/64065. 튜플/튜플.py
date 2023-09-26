def solution(s):
    answer = []
    result = []
    s = s[1:-1]
    arr = list(s.split(','))
    
    for i in range(len(s)) :
        if s[i] == '{' :            
            temp = []
            for j in range(i+1,len(s)) :
                if s[j] == '}' :
                    break
                if s[j] != '{' :
                    temp.append(s[j])
                
                # elif s[j] != ',' :
                #     temp.append(s[j])
            if ',' in temp :
                temp = list(''.join(temp).split(','))
            else :
                temp = list(''.join(temp).split())
            answer.append(temp)
            
            # for t in temp :
            #     if int(t) not in answer :
            #         answer.append(int(t))

    answer.sort(key=len)
    for i in range(len(answer)) :
        for j in range(len(answer[i])) :
            if int(answer[i][j]) not in result :
                result.append(int(answer[i][j]))
    return result