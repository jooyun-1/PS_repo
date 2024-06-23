N = int(input())

row = [0] * N
answer = 0

def promising(x) :
    for i in range(x) :
        if row[x] == row[i] or abs(row[x] - row[i]) == (x-i) :
            return False
    return True
def dfs(x) :
    global answer
    if x == N :
        answer += 1
        return
    else :
        for i in range(N) :
            row[x] = i # 모든 열에 놓음
            if promising(x) : # 다음 행에서 유망할 때
                dfs(x+1) # 모든 행 검사
dfs(0)
print(answer)