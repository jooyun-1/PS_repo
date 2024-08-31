import sys
from collections import Counter

t = int(sys.stdin.readline())
count = {}

for i in range(t) :
    n = int(sys.stdin.readline())
    teams = list(map(int,sys.stdin.readline().split()))
    counter = Counter(teams)
    scores = {}
    rank = 1
    for i in range(n) :
        if counter[teams[i]] == 6 :
            if teams[i] in scores :
                scores[teams[i]].append(rank)
            else :
                scores[teams[i]] = [rank]
            rank += 1
    print(sorted(scores, key = lambda x:(sum(scores[x][0:4]), scores[x][4]))[0])
