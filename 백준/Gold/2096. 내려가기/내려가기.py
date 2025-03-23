from sys import stdin

N = int(input())
# 맨 처음 세개의 숫자를 입력받아 DP의 초기 값을 설정한다.
arr = list(map(int, stdin.readline().split()))
maxDP = arr
minDP = arr

for i in range(N-1) :
    temp = list(map(int, stdin.readline().split()))
    maxDP = [temp[0] + max(maxDP[0],maxDP[1]), temp[1] + max(maxDP), temp[2] + max(maxDP[1],maxDP[2])]
    minDP = [temp[0] + min(minDP[0],minDP[1]), temp[1] + min(minDP), temp[2] + min(minDP[1],minDP[2])]
print(max(maxDP),min(minDP))