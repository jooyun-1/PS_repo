def promising(current_pos,col):
    current_row = len(current_pos)
    for queen_row in range(current_row):
        if current_pos[queen_row] == col or abs(current_pos[queen_row] - col == current_row - queen_row) :
            return False
    return True

def dfs(N, current_row, current_pos, result):
    if current_row == N :
        result.append(current_pos[:]) #얇은 복사?
        return
    
    for col in range(N):
        if promising(current_pos, col): #수직, 대각선 체크
            current_pos.append(col)
            DFS(N,current_row + 1, current_pos, result)
            current_pos.pop()
def n_queen(N):
    result = []
    dfs(N,0,[],result)
    return result