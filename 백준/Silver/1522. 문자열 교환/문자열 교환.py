s = input()
a = s.count('a')

s += s
minVal = float('inf')
for i in range(len(s)-a) :
    minVal = min(minVal, s[i:i+a].count('b'))
print(minVal)