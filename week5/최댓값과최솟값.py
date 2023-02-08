def solution(s):
    answer = ''
    arr = s.split(' ')
    maxVal = float('-inf') # 음수의 무한대
    minVal = float('inf') # 양수의 무한대
    
    for i in arr :
        i = int(i)
        maxVal = max(i,maxVal)
        minVal = min(i,minVal)
    answer += str(minVal) +' '+ str(maxVal)
    return answer