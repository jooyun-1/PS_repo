import sys
from collections import defaultdict
N, M = map(int,sys.stdin.readline().split())
words = list()
word_dic = defaultdict(int)
for i in range(N) :
    s = sys.stdin.readline().rstrip()
    if len(s) >= M :
        if s not in word_dic :
            word_dic[s] = 1
        else :
            word_dic[s] += 1
word_dic = sorted(word_dic.items(), key=lambda item: (-item[1], -len(item[0]), item[0]))
for word, cnt in word_dic :
    print(word)


