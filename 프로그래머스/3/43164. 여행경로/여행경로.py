from collections import defaultdict

def solution(tickets):
    t_dict = defaultdict(list)
    
    # key: 출발지, value: 목적지인 딕셔너리 만듦
    for s, e in tickets:
        t_dict[s].append(e)

    # 목적지 기준 내림차순 정렬(맨 오른쪽걸 pop해서 쓸거임. 알파벳 순서 상 가장 앞선 것)
    for t_key in t_dict.keys():
        t_dict[t_key].sort(reverse = True)
    
    answer = []
    path = ["ICN"]
    
    while path:
        now = path[-1]
        
        if now not in t_dict or len(t_dict[now]) == 0:
            answer.append(path.pop())
        else:
            path.append(t_dict[now].pop())
                         
    return answer[::-1]