# 1. Summary
# 배열 A, B 길이가 같음
# 각각 한 개의 숫자를 뽑아 두 수를 곱한다. => 배열의 길이 만큼 반복 + 두 수를 곱한 값을 누적하여 더한다.
# 이 값을 최소로 만드는 것이 목표

def solution(A,B):
    answer = 0
    cnt = len(A)
    A.sort()
    B.sort(reverse = True)
    for i in range(cnt) :
        answer += (A[i] * B[i])
    # for i in range(cnt) :
    #     answer += (max(A) * min(B))
    #     A.remove(max(A))
    #     B.remove(min(B))
    return answer