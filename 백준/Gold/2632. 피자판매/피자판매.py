import sys

target = int(sys.stdin.readline().rstrip())
m, n = map(int, sys.stdin.readline().split())
A, B = [], []
for i in range(m) :
    A.append(int(sys.stdin.readline().rstrip()))
for i in range(n) :
    B.append(int(sys.stdin.readline().rstrip()))

a_sum, b_sum = [0]*2000001, [0]*2000001 # 최대 크기까지 0으로 초기화
a_sum[0] = b_sum[0] = 1 # 0인 크기 1로 설정 (마지막에 답 낼 때, a 가능한 수 * b 가능한 수 곱해야되므로)

# A, B 가능한 크기마다 개수 + 1
for i in range(len(A)):
    size = 0
    for j in range(len(A)):
        size += A[(i+j) % m]
        if size > target:
            break
        else:
            a_sum[size] += 1

for i in range(len(B)):
    size = 0
    for j in range(len(B)):
        size += B[(i+j) % n]
        if size > target:
            break
        else:
            b_sum[size] += 1 # size마다 카운팅 + 1

a_sum[sum(A)] = b_sum[sum(B)] = 1 # 최종값 1로 세팅

ans = 0
for i in range(target+1):
    ans += (a_sum[i] * b_sum[target-i])
print(ans)