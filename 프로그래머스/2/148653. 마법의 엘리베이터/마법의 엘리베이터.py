
# def get_stones(num,cnt) :
#     print(num,cnt)
#     str_num = str(num)
#     if len(str_num) == 1 :
#         if num > 5 :
#             cnt += (10 - num) + 1
#         else :
#             cnt += num
#         return cnt
#     prev = int(str_num[0])
#     next = int(str_num[0]) + 1
#     if (num - (prev*(10**(len(str_num)-1)))) > (next*(10**(len(str_num)-1)) - num) :
#         return get_stones(next*(10**(len(str_num)-1)) - num, cnt + next)
#     else :
#         return get_stones(num - (prev*(10**(len(str_num)-1))), cnt + prev)
    
def solution(storey):
    answer = 0
    
    while storey:
        div = storey % 10
        if div==5 and storey//10%10>=5 or div>5:
            # 5일 경우는 10의 자리를 조사하여 10의 자리가 5보다 같거나 큰 경우에만 더해주도록 한다
            storey += 10-div
            answer += 10-div
        else:
            answer += div
        storey = storey // 10
        
    return answer
