def solution(numbers):
    answer = ''
    numbers = list(map(str,numbers))
    
    numbers = list(sorted(numbers,key = lambda x : x * 3, reverse = True))
    for i in numbers:             
        answer += i
    
    return str(int(answer))