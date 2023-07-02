T = int(input())

for t in range(T) :
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    answer, temp = [], []
    for n in range(3) :
        temp = []

        for i in range(N) :
            line = []

            for j in range(N-1,-1,-1) :
                line.append(arr[j][i])
            
            temp.append(line)

        arr = temp
        answer.append(temp)
    print('#{}'.format(t+1))
    for i in range(N) :
        for j in range(3) :
            if j == 2 :
                print("".join(map(str,answer[j][i])),end="")
            else :
                print("".join(map(str,answer[j][i])),end=" ")
        print()