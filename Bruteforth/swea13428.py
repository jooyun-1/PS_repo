t = int(input())

for test in range(1,t+1) :
    num = list(input())
    min_num,max_num = ''.join(num),''.join(num)

    for i in range(len(num)-1) :
        for j in range(i+1,len(num)) :
            if i==0 and num[j]=='0':
                continue

            num[i],num[j]=num[j],num[i]
            min_num = min(min_num,''.join(num))
            max_num = max(max_num, ''.join(num))
            num[i],num[j]=num[j],num[i] #숫자 1번만 바꿀수있음으로 원상태로 복귀 
    print('#{} {} {}'.format(test,min_num, max_num))