def solution(answers):
    answer = []
    supo1 = [1,2,3,4,5]
    supo2 = [2,1,2,3,2,4,2,5]
    supo3 = [3,3,1,1,2,2,4,4,5,5]
    cnt1, cnt2 , cnt3 = 0, 0, 0
    
    for i in range(len(answers)) :
        index1, index2, index3 = i % 5, i % 8, i % 10
        
        if answers[i] == supo1[index1] :
            cnt1 += 1
        if answers[i] == supo2[index2] :
            cnt2 += 1
        if answers[i] == supo3[index3] :
            cnt3 += 1
    
    result = max(cnt1, cnt2, cnt3)
    
    if result == cnt1 :
        answer.append(1)
    if result == cnt2 :
        answer.append(2)
    if result == cnt3 :
        answer.append(3)
    
    return answer    
