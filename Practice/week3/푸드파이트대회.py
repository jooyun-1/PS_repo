def solution(food):
    answer = ''
    for i in range(1, len(food)):
        answer += str(i)*(food[i] // 2)
    reversed_food = ''.join(reversed(list(answer)))
    answer += '0'    
    answer += reversed_food
    return answer