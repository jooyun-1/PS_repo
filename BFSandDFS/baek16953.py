# A -> B
# A = A * 2
# A = int("A1")
import sys
A, B = map(int,sys.stdin.readline().split())
que= []
# visited = []
visited = dict()
cnt = 1
def bfs(node) :
    global cnt
    que.append(node)
    # visited[node] = 
    # visited.append(node)
    visited[node] = cnt
    while que:
        next = que.pop(0)
        if next == B :
            return visited[next]
        for num in (2*next, int(str(next) +"1")) :
            if 0<=num<=B and num not in visited.keys() :
                que.append(num)
                visited[num] = visited[next] + 1
    return -1
print(bfs(A))
