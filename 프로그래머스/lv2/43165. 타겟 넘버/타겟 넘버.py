answer = 0
def dfs(numbers,num,cnt,target) :
    global answer

    if cnt == len(numbers):
        if num == target :
            answer += 1
        return

    dfs(numbers,num + numbers[cnt],cnt+1,target)
    dfs(numbers,num - numbers[cnt],cnt+1,target)
            
def solution(numbers, target): 
    global answer
    dfs(numbers,0,0,target)
    return answer