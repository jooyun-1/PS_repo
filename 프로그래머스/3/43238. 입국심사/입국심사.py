def solution(n, times):
    answer = 0
    left, right = 1, max(times) * n
    while left <= right :
        mid = (left + right) // 2
        people = 0
        for time in times :
            # people 은 모든 심사관들이 mid분 동안 심사한 사람의 수
            people += mid // time
            # # 모든 심사관을 거치지 않아도 mid분 동안 n명 이상의 심사를 할 수 있다면 반복문을 나간다.
            # if people >= n:
            #     break 
        if people >= n :
            answer = mid
            right = mid - 1
        elif people < n :
            left = mid + 1
    return answer