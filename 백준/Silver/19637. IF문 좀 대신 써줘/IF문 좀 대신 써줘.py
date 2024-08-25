import sys

N, M = map(int,sys.stdin.readline().split())
menu = []

for i in range(N) :
    a, b = sys.stdin.readline().split(' ')
    menu.append([a, int(b)])

menu.sort(key=lambda x : x[1])

for j in range(M) :
    temp = int(sys.stdin.readline().rstrip())
    start = 0
    end = len(menu) - 1
    while start <= end :
        mid = (start + end) // 2
        if temp > menu[mid][1]:
            start = mid + 1
        else:
            end = mid - 1
    print(menu[start][0])
