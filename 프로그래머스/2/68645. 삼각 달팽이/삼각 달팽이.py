def solution(n):
    answer = [] 
    arr = [[0] * i for i in range(1,n+1)]
    max_num = sum (i for i in range(1,n+1))
    dir = [[1,0],[0,1],[-1,-1]]
    turn = 0
    x, y = 0, 0
    i = 1
    while i <= max_num :
        arr[x][y] = i
        i += 1
        dx, dy = dir[turn][0], dir[turn][1]
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0 :
            x, y = nx, ny
        else :
            turn = (turn + 1) % 3
            dx, dy = dir[turn][0], dir[turn][1]
            x += dx
            y += dy
    for row in arr :
        for i in range(len(row)) :
            answer.append(row[i])
    return answer