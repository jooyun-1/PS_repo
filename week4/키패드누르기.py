# 맨 처음 왼쪽: * 오른쪽: #
# 상하좌우 4방향 1칸 이동
# 1, 4, 7 => 왼쪽 
# 3, 6, 9 => 오른쪽
# 2, 5, 8, 0 => 더 가까운 쪽 (같으면 잡이에 따라 다름)
def solution(numbers, hand):
    answer = ''
    left= '*'   ## 초기 왼손 위치
    right = '#'  ## 초기 오른손 위치

    keypad = {1 : [0,0], 2 : [0,1], 3 : [0,2], 
              4 : [1,0], 5 : [1,1], 6 : [1,2], 
              7 : [2,0], 8 : [2,1], 9 : [2,2],
              '*':[3,0], 0 : [3,1], '#':[3,2]}
              
    for num in numbers:
        if num in [1,4,7]:   
            answer += 'L'
            left = num
        elif num in [3,6,9]: 
            answer += 'R'
            right = num
        else:			
            left_pos = keypad[left]  
            right_pos = keypad[right] 
			
            left_dist = abs(left_pos[0] - keypad[num][0]) + abs(left_pos[1] - keypad[num][1])
            right_dist = abs(right_pos[0] - keypad[num][0]) + abs(right_pos[1] - keypad[num][1])
            
            if left_dist < right_dist : 
                answer += 'L'
                left = num
            elif left_dist > right_dist :
                answer += 'R'
                right = num
            else:						
                if hand == 'left':
                    answer += 'L'
                    left = num
                else:
                    answer += 'R'
                    right = num
    return answer