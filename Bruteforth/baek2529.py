import sys
N = int(sys.stdin.readline())
sign = list(sys.stdin.readline().split())
visited = [0] * 10
minVal = ""
maxVal = ""

def check(i,j,k) :
    if k == "<" :
        return i < j
    else :
        return i > j

def solve(n, s) :
    global minVal, maxVal

    if n == N+1 :
        if len(minVal) == 0 :
            minVal = s
        else :
            maxVal = s
        return
    
    for i in range(10) :
        if not visited[i] :
            if n == 0 or check(s[-1],str(i),sign[n-1]) :
                visited[i] = 1
                solve(n+1, s+str(i))
                visited[i] = 0
solve(0, "")
print(maxVal)
print(minVal)
