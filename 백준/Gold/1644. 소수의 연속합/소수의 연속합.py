N = int(input())

a = [False, False] + [True] * (N-1)
prime_num = []

for i in range(2,N+1) :
    if a[i] :
        prime_num.append(i)
        for j in range(2*i, N+1, i) :
            a[j] = False
answer, start, end = 0, 0, 0
total = 0
while True :
    if total == N :
        answer += 1
    
    if total > N :
        total -= prime_num[start]
        start += 1
    elif end == len(prime_num) :
        break
    else :
        total += prime_num[end]
        end += 1
print(answer)