def solution(N, stages):
    answer = []
    temp = {}
    stages_len = len(stages)

    for i in range(1, N+1) :
        if stages_len !=0 :
            temp [i] = stages.count(i) / stages_len
            stages_len -= stages.count(i)
        else :
            temp[i] = 0    
    answer = sorted(temp, key = lambda a : temp[a] , reverse = True)
    return answer