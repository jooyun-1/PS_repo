t = int(input())

for test in range(1,t+1) :
    s = input().rstrip()
    arr = list(s)
    arr.sort()
    # for i in range(len(s)-1) :
    #     if s[i] == s[i+1] :
    #         s = s[i+2:]
    i = 0
    while True :
        if len(arr) == 0:
            print('#{} {}'.format(test,'Good'))
            break
        if i == len(arr) -1 :
            break
        if arr[i] == arr[i+1] :
            del arr[i:i+2]
            i = 0
        else :
            i += 1
    if len(arr) > 0 :
        print('#{} {}'.format(test, ''.join(arr)))
