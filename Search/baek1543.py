docu = input()
word = input()
index, cnt = 0, 0
while len(docu) >= index+len(word) :
    if docu[index:index+len(word)] == word :
        cnt += 1
        index += len(word)
    else :
        index += 1
print(cnt)

