# 바구니의 가장 아래칸부터 쌓임
# 같은 모양이 쌓이면 없어짐
# 1,5,3,5,1,2,1,4
def solution(board, moves):
    answer = 0
    basket = []
    for i in moves:
        for j in range(len(board)):            
            if board[j][i-1] > 0 :
                basket.append(board[j][i-1])
                board[j][i-1] = 0 
                if len(basket) > 1:
                    if basket[-2] == basket[-1]:
                        basket.pop(-2)
                        basket.pop(-1)
                        answer += 2
                break # 처음 만난 인형만 처리해주면 됨
    return answer