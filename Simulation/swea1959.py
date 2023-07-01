T = int(input())


for t in range(T) :
    N, M = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    answer = 0
    sum, index = 0, 0
    if len(a) == len(b) :
        for i in range(len(a)) :
            sum += a[i] * b[i]
        answer = sum
    else :
        if N < M :

            while True :
                if index > len(b)-len(a) :
                    break
                temp = index
                sum = 0
                for i in range(len(a)) :
                    sum += a[i] * b[index]
                    index += 1
                answer = max(sum, answer)
                index = temp + 1
                           
        elif N > M :
            while True :
                if index > len(a)-len(b) :
                    break
                temp = index
                sum = 0
                for i in range(len(b)) :
                    sum += b[i] * a[index]
                    index += 1
                answer = max(sum, answer)
                index = temp + 1
    print('#{} {}'.format(t+1,answer))