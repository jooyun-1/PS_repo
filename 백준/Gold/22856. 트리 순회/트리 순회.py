import sys
sys.setrecursionlimit(1000000)
N = int(sys.stdin.readline())
parent = dict()
left = dict()
right = dict()
cnt = 0
for n in range(N) :
    node, l, r = map(int, sys.stdin.readline().split())
    left[node] = l
    right[node] = r

    if l != -1 :
        parent[l] = node
        cnt += 1
    if r != -1 :
        parent[r] = node
        cnt += 1
last = 0
def search(node) :
    global last
    if node == - 1:
        return
    search(left[node])
    last = node
    search(right[node])

search(1)
edge_cnt = cnt * 2
move = 0
while last != 1 :
    move += 1
    last = parent[last]
print(edge_cnt - move)
