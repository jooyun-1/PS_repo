from collections import deque

# 시간을 str에서 int형태로 변환하는 함수
def get_int(plan):
    subject, start, playtime = plan
    
    a, b = start.split(":")
    
    start = int(a)*60 + int(b)
    
    playtime = int(playtime)
    
    return subject, start, playtime

def solution(plans):
    answer = []
    
    # 시간 순서대로 정렬
    plans.sort(key = lambda x : x[1])

    st = []
    
    plans_idx = 1
    
    now_subject, now_start, now_playtime = get_int(plans[0])
    
    while 1:
        next_subject, next_start, next_playtime = get_int(plans[plans_idx])
        
        # 새로운 과제 시작시간이 진행 중이던 과제 끝나는 시간보다 빠르면 -> 진행 중 과제 멈추고 새로운 과제 시작
        if next_start < now_start + now_playtime:
            st.append((now_subject, now_start + now_playtime - next_start))
            now_subject, now_start, now_playtime = next_subject, next_start, next_playtime
            plans_idx += 1
            
        # 그렇지 않다면 진행 중 과제 마치고. 멈춰둔 과제 or 새로 시작해야 하는 과제해야되는지 결정
        else:
            answer.append(now_subject)
              
            # 멈춰둔 과제가 있는 경우
            if st:
                # 과제를 끝낸 시각에 새로 시작해야 되는 과제와 잠시 멈춰둔 과제가 모두 있다면, 새로 시작해야하는 과제부터 진행
                if next_start == now_start + now_playtime:
                    now_subject, now_start, now_playtime = next_subject, next_start, next_playtime
                    plans_idx += 1     
                else:
                    subject, remain_playtime = st.pop()
                    print(subject,now_start,now_playtime,now_start + now_playtime,remain_playtime)
                    now_subject, now_start, now_playtime = subject, now_start + now_playtime, remain_playtime
                     
            # 멈춰둔 과제가 없다면 새로 시작해야 하는 과제 시작
            else:
                now_subject, now_start, now_playtime = next_subject, next_start, next_playtime
                plans_idx += 1 
        
        # 새로 배울게 없다면 진행중인 과제 마무리
        if plans_idx == len(plans):
            answer.append(now_subject)
            break
    
    # 최근에 멈춘 과제부터 마무리
    for subject, _ in st[::-1]:
        answer.append(subject)
        
    return answer