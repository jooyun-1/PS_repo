import sys
N = int(sys.stdin.readline())
arr = [0] * (N+1)
for i in range(1,N+1) :
    arr[int(sys.stdin.readline())] += 1 # 입력숫자와 동일한 인덱스 1씩 높여줌
for a in range(1,N+1) :
    for b in range(arr[a]) : # 1부터 arr에 있는 개수대로 출력
        print(a)