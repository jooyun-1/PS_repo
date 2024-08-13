import sys

n, m = map(int, sys.stdin.readline().split())
dic = dict()
answer = 0
for i in range(n) :
    word = sys.stdin.readline().rstrip()
    dic[word] = 1
    answer += 1

for i in range(m) :
    line = list(sys.stdin.readline().rstrip().split(','))
    for w in line :
        if w in dic.keys() :
            if dic[w] == 1 :
                dic[w] = 0
                answer -= 1
    print(answer)