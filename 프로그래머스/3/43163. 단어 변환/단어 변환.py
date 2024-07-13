def solution(begin, target, words):
    global answer, flag
    answer = 51
    visited = [0] * len(words)
    flag = False
    def dfs(s, result) :
        global answer,flag
        # print(s,visited)
        if s == target :
            flag = True
            answer = min(answer,result)
            # return result
        for i in range(len(words)) :
            # print(words[i])
            cnt = 0
            for j in range(len(begin)) :
                if s[j] != words[i][j] :
                    cnt += 1
                if cnt > 1 :
                    break
            if cnt == 1 and visited[i] == 0:
                visited[i] = 1
                dfs(words[i], result + 1)
                visited[i] = 0            
    dfs(begin,0)
    if flag == False :
        return 0
    return answer