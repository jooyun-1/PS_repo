# 4개 지표, 각 지표 유형 2개
# n개의 질문, 선택지 7개
# 각 질문, 1가지 지표로 점수 매김
# 매우 동의, 매우 비동의 => 3점 | 동의, 비동의 => 2점 | 약간 동의, 약간 비동의 => 1점, 모르겠음 => X 
# 각 지표에서 더 높은 점수를 받은 성격 유형 or 점수 같으면 사전 순으로 빠른 성격 유형
# 앞 : 비동의 , 뒤 : 동의
def solution(survey, choices):
    answer = ''
    temp = ''
    score = { 1 : 3, 2 : 2, 3 : 1, 4 : 0, 5 : 1, 6 : 2 , 7 :3}
    surveyList = { 1 : ['R', 'T'], 2: ['C', 'F'], 3: ['J', 'M'], 4: ['A', 'N']}
    for i in range(len(survey)) :
        if choices[i] > 4 :
            temp += survey[i][1] * score[choices[i]]
        if choices[i] < 4 :
            temp += survey[i][0] * score[choices[i]]
    for j in surveyList :
        if temp.count(surveyList[j][0]) > temp.count(surveyList[j][1]):
            answer += surveyList[j][0]
        elif temp.count(surveyList[j][1]) > temp.count(surveyList[j][0]):
            answer += surveyList[j][1]
        else :
            if surveyList[j][1] > surveyList[j][0] :
                answer += surveyList[j][0]
            else :
                answer += surveyList[j][1]
    return answer