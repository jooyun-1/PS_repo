import sys

n = int(sys.stdin.readline())
triangle = []
for i in range(n) :
    line = list(map(int, sys.stdin.readline().split()))
    triangle.append(line)

for i in range(1,len(triangle)) :
    for j in range(len(triangle[i])) :
        if j == 0 :
            triangle[i][j] += triangle[i-1][j]
        elif j == len(triangle[i]) - 1 :
            triangle[i][j] += triangle[i-1][j-1]
        else :
            triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
answer = max(triangle[-1])
print(answer)