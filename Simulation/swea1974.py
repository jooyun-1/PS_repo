T = int(input())

for t in range(T) :
    arr = [list(map(int,input().split())) for _ in range(9)]
    flag = 1
    for i in range(9) :
        temp, temp2 = [],[]
        if flag == 0 :
            break
        for j in range(9) :
            if arr[i][j] in temp :
                flag = 0
                break
            if arr[j][i] in temp2 :
                flag = 0
                break
            temp.append(arr[i][j])
            temp2.append(arr[j][i])
    index = 0
    while index < 9 :
        temp3 = []
        for i in range(index,index+3) :
            for j in range(index,index+3) :
                if arr[i][j] in temp3 :
                    flag = 0
                    break
                temp3.append(arr[i][j])
        index += 3
    print('#{} {}'.format(t+1,flag))