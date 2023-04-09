import sys
sys.setrecursionlimit(100000)
N, M, P = map(int,sys.stdin.readline().split())
arr = [[] for _ in range(M+1)]
visited = [[] for _ in range(M+1) ]
cnt = 0
for i in range(N) :
    a, b = map(int, sys.stdin.readline().split())
    arr[b].append(a)
    visited[b].append(0)

def bfs(hate) :
    global cnt
    que = []
    que.append(hate)
    while que :
        h = que.pop(0)
        for i in range(len(arr[h])) :
            if visited[h][i] == 0 and arr[h][i] != 0:
                visited[h][i] = 1
                que.append(arr[h][i])
                cnt += 1
                break
            if visited[h][i] == 1 :
                return -1
    return cnt
print(bfs(P))

# while True :
#     flag = True
#     if 0 not in visited :
#         cnt = -1
#         break
#     for i in range(len(arr)) :
#         if hate == arr[i][1] :
#             visited[i] = 1
#             hate = arr[i][0]
#             flag = False
#             break
#     if flag == True :
#         break
#     cnt += 1
