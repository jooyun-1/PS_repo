T = int(input())

for t in range(T) :
    i = input()
    arr = [0] * 101
    score = list(map(int,input().split()))
    index = 0
    for sc in score :
        arr[sc] += 1 
        if arr[sc] >= arr[index] :
            index = sc
    print('#{} {}'.format(t+1,index))