# 아직 보여주지 않은 문자 중 추가했을 때의 문자열이
# 사전 순으로 가장 앞에 오도록 하는 문자를 보여주는 것
import sys

input = sys.stdin.readline().rstrip()
answer = [''] * len(input)

def search(s, start) :
    if s == "" :
        return
    ch = min(s)
    idx = s.index(ch)
 
    answer[start + idx] = ch
    print(''.join(answer))
    
    search(s[idx + 1 :], start + idx + 1)
    search(s[:idx],start)
search(input, 0)