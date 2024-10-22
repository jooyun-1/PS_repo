def solution(numbers, target):
    global answer
    answer = 0
    arr = [1,-1]
    def dfs(num, cnt) :
        global answer
        if cnt == len(numbers) :
            if num == target :
                answer += 1
            return 
        for i in range(len(arr)) :
            dfs(num + arr[i] * numbers[cnt], cnt + 1)
    dfs(0,0)
    return answer