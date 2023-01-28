def solution(lottos, win_nums):
    answer = []
    rank = {
        6 : 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6
    }
    count, zero_cnt = 0,0
    for num in lottos :
        if num == 0:
            zero_cnt += 1
        count += win_nums.count(num)        
    max_ranking = rank[count+zero_cnt]
    answer.append(max_ranking)
    answer.append(rank[count])
    return answer