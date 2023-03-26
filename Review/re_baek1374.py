import sys
import heapq
N = int(sys.stdin.readline())
arr, room = [], []
for i in range(N) :
    num, start, end = map(int,sys.stdin.readline().split())
    heapq.heappush(arr,[start,end])

startTime, endTime = heapq.heappop(arr)
heapq.heappush(room,endTime)

while arr :
    start, end = heapq.heappop(arr)
    if room[0] <= start :
        heapq.heappop(room)
    heapq.heappush(room,end)
print(len(room))

