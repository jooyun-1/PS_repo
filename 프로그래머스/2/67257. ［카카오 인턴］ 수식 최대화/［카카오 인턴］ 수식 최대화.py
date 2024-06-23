from itertools import permutations

def solution(expression):
    # 연산자 우선 순위가 6종류밖에 안 되고, expression 길이도 짧습니다.
    # brute-force
    values = []

    for priority in permutations(['*', '+', '-'], 3):
        # 우선 연산자와 피연산자를 저장해두고,
        operands = []
        temp = ''
        for e in expression :
            if e.isdigit() :
                temp += e
            else :
                operands.append(int(temp))
                temp = ''
        if len(temp) > 0 :
            operands.append(int(temp))

        operators = [c for c in expression if c in '*+-']
        
        # 우선순위대로 연산을 수행합니다.
        for op in priority:
            
            while op in operators:
                # i번째 연산자는 i번째 피연산자와 i+1번째 피연산자에 대한 연산을 수행합니다.
                i = operators.index(op)
                
                if op == '*':
                    v = operands[i] * operands[i+1]
                elif op == '+':
                    v = operands[i] + operands[i+1]
                else:
                    v = operands[i] - operands[i+1]
                
                # 피연산자 리스트를 업데이트 합니다.
                operands[i] = v
                operands.pop(i+1)
                # 연산자 리스트를 업데이트 합니다.
                operators.pop(i)
        
        values.append(operands[0])
        
    return max(abs(v) for v in values)