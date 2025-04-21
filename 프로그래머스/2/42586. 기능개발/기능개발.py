# 각 기능 : 진도 100% -> 서비스 반영
# 기능 개발 속도 다름
# 앞에 있는 기능 배포될 때 함께 배포 (뒤에 있는 기능이 먼저 개발되면)

def solution(progresses, speeds):
    answer = []
    index = 0

    while True :
        cnt = 0
        if len(progresses) == sum(answer) :
            break
        for i in range(len(progresses)) :
            progresses[i] += speeds[i]
        if progresses[index] >= 100 :
            cnt += 1
            for j in range(index,len(progresses)) :
                if progresses[j] >= 100 :
                    cnt += 1
                else :
                    break
        if cnt > 0 :
            answer.append(cnt-1)
            index += cnt - 1

    return answer