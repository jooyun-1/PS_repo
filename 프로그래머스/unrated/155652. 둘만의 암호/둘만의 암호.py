# s의 각 알파벳을 index만큼 뒤의 알파벳으로 바꾼다
# index만큼의 뒤의 알파벳이 z를 넘어가면 a로 돌아감
# skip에 있는 알파벳은 제외하고 건너뜀

def solution(s, skip, index):
    answer = ''
    for c in s :
        i = ord(c)
        j = index
        while j > 0 :
            i += 1
            if chr(i) >= 'z' :
                i = ord('a')
            if chr(i) in skip :
                j += 1
            j -= 1
        answer += chr(i)
    return answer