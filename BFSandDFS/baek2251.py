import sys
a, b, c = map(int,sys.stdin.readline().split())
que = []
N = 201
visited = [[0] * (N) for _ in range(N)]
answer = []

def pour(x,y) :
    if visited[x][y] == 0 :
        visited[x][y] = 1
        que.append((x,y))
def bfs() :
    que.append((0,0))
    visited[0][0] = 1
    while que :
        x, y = que.pop(0)
        z = c- x- y
        if x == 0 :
            answer.append(z)
        # a -> b
        water = min(x,b-y)
        pour(x-water,y+water)

        # a-> c
        water = min(x,c-z)
        pour(x-water,y)

        # b-> c
        water = min(y,c-z)
        pour(x, y - water)
        # b-> a
        water = min(y,a-x)
        pour(x + water, y - water)
        
        # c->a
        water = min(z,a-x)
        pour(x + water, y)
        # c->b
        water = min(z,b-y)
        pour(x, y + water)

bfs()
answer.sort()

for ans in answer :
    print(ans, end = " ")
# que = [[a, 0, c-a],[0,b,c-b]]
# for i in range(len(que)) :
#     arr.append(list(permutations(que[i],3)))

# for i in range(len(arr)) :
#     for j in range(len(arr[i])) :
#         if arr[i][j][2] > 0 and arr[i][j][2] not in answer :
#             answer.append(arr[i][j][2])
# answer.sort()
# for ans in answer :
#     print(ans, end= " ")
