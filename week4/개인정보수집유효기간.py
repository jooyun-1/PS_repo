# 개인정보 1~n
# 각 약관마다 유효기간 있음
# 모든 달은 28일까지 있다
def dateToSum(date):
    year, month, day = map(int, date.split("."))
    return (year * 12 * 28) + (month * 28) + day # 날짜를 아예 일수로 바꿔 합산 
    
def solution(today, terms, privacies):
    answer = []    
    today = dateToSum(today)    
    terms_dict = {}
    for term in terms:
        term = term.split()
        terms_dict[term[0]] = int(term[1]) * 28

    for i in range(len(privacies)):
        date, term = privacies[i].split()
        if dateToSum(date) + terms_dict[term] <= today:
            answer.append(i+1)
        
    return answer
