import sys
T = int(sys.stdin.readline())

final = []

def operator(now, ans) :
     global answer
     if now == n+1 :
          calc(ans)
          return
     operator(now+1, ans + ' ' + str(now))
     operator(now+1, ans + '+' + str(now))
     operator(now+1, ans + '-' + str(now))

def calc(ans) :
     temp = ans.replace(' ','')
     if eval(temp) == 0 :
          answer.append(ans)

for i in range(T) :
     n = int(sys.stdin.readline())
     answer = []
     operator(2, '1')
     final.append(answer)
for f in final :
     for i in range(len(f)) :
          print(''.join(f[i]))
     print()
