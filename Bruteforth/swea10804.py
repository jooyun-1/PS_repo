t = int(input())

for test in range(1,t+1) :
    arr = list(input().rstrip())
    arr.reverse()

    for i in range(len(arr)) :
        if arr[i] == 'q' :
            arr[i] = 'p'
        elif arr[i] == 'p' :
            arr[i] = 'q'
        elif arr[i] == 'b' :
            arr[i] = 'd'
        elif arr[i] == 'd' :
            arr[i] = 'b'
    print('#{} {}'.format(test, ''.join(arr)))