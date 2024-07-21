def solution(sizes):
    answer = 0
    row, col = 0, 0
    for s in sizes :
        if s[0] < s[1] :
            temp = s[0]
            s[0] = s[1]
            s[1] = temp
    for s in sizes :
        row = max(row,s[0])
        col = max(col,s[1])
    print(row, col)
    return row * col