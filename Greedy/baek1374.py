# 최대한 적은 수의 강의실 => 모든 강의
# 한 강의실 => 동시에 2개 이상의 강의 진행 X
import sys
import heapq
N = int(sys.stdin.readline())
lecture = []
room = []

cnt = 0
for i in range(N) :
    num, start, end = map(int,sys.stdin.readline().split())
    heapq.heappush(lecture, [start,end,num])

start, end, num = heapq.heappop(lecture)
heapq.heappush(room, end)

while lecture:
    start, end, num = heapq.heappop(lecture)
    if room[0] <= start:
        heapq.heappop(room)
    heapq.heappush(room, end)

print(len(room))

#     if a in lecture.keys() :
#         lecture[a] = min(lecture[a],b)
#         answer.append(a)
#     lecture[a] = b
# temp = max(lecture.keys())

# for val in lecture.values():
#     print(val)
#     for key in lecture.keys() :
#         if val < key :
#             temp = min(key,temp)
#     # cnt += 1
#     lecture[temp] = max(lecture.keys())
#     answer.append(temp)
# print(answer)  

# print(lecture)

