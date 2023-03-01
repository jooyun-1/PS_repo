# 집 N개 1번~N번
# R,G,B 중 하나의 색으로 칠해야함
# 각각의 집을 칠하는 비용이 주어짐
# 1번 집의 색 != 2번 집의 색
# N번 집의 색 != N-1번 집의 색
# i-1번 집의 색 != i-1, i+1번 집의 색
# 1행부터 탐색 => 안 겹치는 두 열 원소 중 작은거 합해줌

### dfs 첫 접근
# import sys
# N = int(sys.stdin.readline())
# costs, answer = [], []
# start, sum = 0, 0
# for i in range(N) :
#     costs.append(list(map(int, sys.stdin.readline().split())))
# # def promising(x,y) :
# temp = 0
# def dfs(x,y) :
#     global sum, minVal,temp
#     minVal = 1001
#     if x == N :
#         print(sum)
#         answer.append(sum)
#         return
#     for i in range(3) :
#         if i != y :
#             minVal = min(minVal,costs[x][i])
#             if costs[x][i] == minVal :
#                 temp = i
#     sum += minVal
#     print(temp, minVal)
#     dfs(x+1,temp) 
# for i in range(3) :
#     sum = costs[0][i]
#     dfs(1,i)
# print(min(answer))
import sys
N = int(sys.stdin.readline())
costs = []

for i in range(N) :
    costs.append(list(map(int, sys.stdin.readline().split())))
dp = [i for i in costs]

for i in range(1, len(costs)) :
    dp[i][0] = min(dp[i-1][1],dp[i-1][2]) +dp[i][0]
    dp[i][1] = min(dp[i-1][0],dp[i-1][2]) +dp[i][1]
    dp[i][2] = min(dp[i-1][0],dp[i-1][1]) +dp[i][2]
print(min(dp[N-1][0],dp[N-1][1],dp[N-1][2])) 

