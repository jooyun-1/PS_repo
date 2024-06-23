def solution(msg):
    answer = []
    dic = {chr(i+64):i for i in range(1, 27)}    
    index = 27

    while True:
        i = 0
        
        if msg in dic:
            answer.append(dic[msg])
            return answer
        else:
            for j in range(1, len(msg)+1):
                if msg[i:j] not in dic:
                    answer.append(dic[msg[i:j-1]])   
                    dic[msg[i:j]] = index
                    index += 1                    
                    msg = msg[j-1:]
                    break