import sys

n, new, p = map(int,sys.stdin.readline().split())

if n :
    scores = list(map(int,sys.stdin.readline().split()))
    scores.append(new)
    scores.sort(reverse=True)
    index = scores.index(new) + 1
    if index > p :
        print(-1)
    else :
        if n == p and scores[-1] == new :
            print(-1)
        else :
            print(index)
else :
    print(1)
