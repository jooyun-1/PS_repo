import sys

s = list(sys.stdin.readline().rstrip())
one_count = s.count('1') // 2
zero_count = s.count('0') // 2
s.sort()
answer = s.copy()
for i in range(len(s)) :

    if s[i] == '0' and zero_count > 0 :
        answer.remove('0')
        zero_count -= 1

    elif s[i] == '1' and one_count > 0 :
        answer.remove('1')
        one_count -= 1

print(''.join(answer))
# print(one_count,zero_count,answer)
