def solution(numbers):
    answer = []
    numbers.sort()
    for i in range(len(numbers)-1) :
        for j in range(i+1, len(numbers)) :
            if numbers[i] + numbers[j] in answer :
                continue
            answer.append(numbers[i] + numbers[j])
    
    answer.sort()
    return answer