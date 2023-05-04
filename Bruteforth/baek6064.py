import sys
t = int(sys.stdin.readline())
for _ in range(t):
    m,n,x,y = map(int,input().split())
    ans = -1
    while x <= m*n:
        if (x-y) % n == 0:
            ans = x
            break
        x += m
    print(ans)   


# answer = []
# for i in range(t) :
#     m, n, x, y = map(int,sys.stdin.readline().split())
#     cnt = 1
#     a,b = 1,1
#     while(True) :

#         if a == m and b == n :
#             answer.append(-1)
#             break
#         if a == x and b == y :
#             answer.append(cnt)
#             break
#         a += 1
#         if a > m :
#             a = 1
#         b += 1
#         if b > n :
#             b = 1
#         cnt += 1
# for ans in answer:
#     print(ans)