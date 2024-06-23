T = int(input())
def combi_to_dp(r,c) :
    if arr[r][c] != 0 :
        return arr[r][c]
    if r == c or c == 0 :
        return 1
    else :
        arr[r][c] = combi_to_dp(r-1,c-1) + combi_to_dp(r-1,c)
        return arr[r][c]
for t in range(T) :
    N, M = map(int,input().split())
    arr = [[0] * (N+1) for _ in range(M+1)]
    print(combi_to_dp(M,N))