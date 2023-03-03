# 가장 많이 팔린 책
import sys
N = int(sys.stdin.readline())
books, answer = [], []
titles = dict()
for i in range(N) :
    books.append(sys.stdin.readline())
for book in books :
    if book in titles.keys() :
        titles[book] += 1
    else :
        titles[book] = 1
for title in titles.keys():
    if titles[title] ==  max(titles.values()) :
        answer.append(title)
answer.sort()
print(answer[0])