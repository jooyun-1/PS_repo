import sys
n, m, k = map(int, sys.stdin.readline().split())
answer = 0
while n >= 2 and m >= 1 and n + m >= k + 3 :
    n -= 2
    m -= 1
    answer += 1
print(answer)
# if n > m :
#     n -= k
#     answer = min(n//2, m)
# else :
#     m -= k
#     answer = min(n//2,m)
