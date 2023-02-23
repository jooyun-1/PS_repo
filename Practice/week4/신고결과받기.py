# 처리 결과 메일 발송
# 한번에 한명의 유저만 신고 가능 (횟수에 제한은 없음, 서로 다른 유저를 계속해서 신고 가능)
# 한 유저를 여러 번 신고 가능(단, 1회로 처리됨)
# k번 이상 신고된 유저는 정지. 해당 유저를 신고한 모든 유저에게 정지 사실 메일 발송
def solution(id_list, report, k):
    answer = []
    report = list(set(report))
    reported_dict = {key : 0 for key in id_list} # 누가 누굴 신고했는지 key , value: 배열
    mail_cnt = {cnt :0 for cnt in id_list}
    for repo in report :
        temp = repo.split(' ')
        reported_dict[temp[1]] += 1    
    for repo in report :
        if reported_dict[repo.split(' ')[1]] >=k :
            mail_cnt[repo.split(' ')[0]] += 1
    return list(mail_cnt.values())