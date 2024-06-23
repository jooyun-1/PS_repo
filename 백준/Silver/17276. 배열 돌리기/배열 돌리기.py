import sys
import copy
# 배열 X를 45도의 배수만큼 시계방향 or 반시계방향으로 turn
# 시계방향
# X의 주 대각선을 ((1,1), (2,2), …, (n, n)) 가운데 열 ((n+1)/2 번째 열)로 옮긴다.
# X의 가운데 열을 X의 부 대각선으로 ((n, 1), (n-1, 2), …, (1, n)) 옮긴다.
# X의 부 대각선을 X의 가운데 행 ((n+1)/2번째 행)으로 옮긴다.
# X의 가운데 행을 X의 주 대각선으로 옮긴다.
# 위 네 가지 경우 모두 원소의 기존 순서는 유지 되어야 한다.
# X의 다른 원소의 위치는 변하지 않는다.

T = int(sys.stdin.readline())

for t in range(T) :
    n, d = map(int,sys.stdin.readline().split())
    arr = []
    flag = True

    for i in range(n) :
        line = list(map(int,sys.stdin.readline().split()))
        arr.append(line)
    change_arr = copy.deepcopy(arr)

    if d > 0 :
        times = d // 45
    else :
        times = abs(d) // 45
        flag = False

    if flag :
        for a in range(times) :
            for i in range(n) :
                change_arr[i][(n+1)//2-1] = arr[i][i]
                change_arr[i][n-i-1] = arr[i][(n+1)//2-1]
                change_arr[(n+1)//2-1][i] = arr[n-i-1][i]
                change_arr[i][i] = arr[(n+1)//2-1][i]
            arr = copy.deepcopy(change_arr)
    else :
        for a2 in range(times) :
            for i2 in range(n) :
                change_arr[n-i2-1][(n + 1)//2-1] = arr[n-i2-1][i2]
                change_arr[i2][i2] = arr[i2][(n+1)//2-1]
                change_arr[(n+1)//2-1][i2] = arr[i2][i2]
                change_arr[i2][n-i2-1] = arr[(n+1)//2-1][n-i2-1]
            arr = copy.deepcopy(change_arr)


    for x in range(len(change_arr)) :
        print(" ".join(map(str,change_arr[x])))