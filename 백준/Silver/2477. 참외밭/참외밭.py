# 동 : 1, 서 : 2, 남 : 3, 북 : 4
import sys

N = int(sys.stdin.readline())
arr = []
w, h = 0, 0
w_index, h_index = 0, 0
for i in range(6) :
    dir, k = map(int,sys.stdin.readline().split())
    arr.append([dir,k])
for i in range(len(arr)):
    if arr[i][0] == 1 or arr[i][0] == 2 :
        if arr[i][1] > w :
            w = arr[i][1]
            w_index = i
    else :
        if arr[i][1] > h :
            h = arr[i][1]
            h_index = i
sum = 0
sum += w * h - abs(arr[(w_index-1) % 6][1] - arr[(w_index + 1) % 6][1]) * abs(arr[(h_index-1) % 6][1] - arr[(h_index + 1) % 6][1])
print(sum * N)