import sys
n = int(sys.stdin.readline())
line = sys.stdin.readline().rstrip()
arr = []

for i in range(len(line)) :
    arr.append(line[i])

colors = {'B' : 0, 'R' : 0}
colors[arr[0]] += 1

for i in range(1,n) :
    if arr[i] != arr[i-1] :
        colors[arr[i]] += 1
work = min(colors['B'], colors['R']) + 1
print(work)
# if arr[0] == 'R' :
#     flag = 'B'
# else :
#     flag = 'R'

# for i in range(len(arr)) :
#     if cnt_r >= cnt_b :
#         if arr[i] == 'B' :
#             if flag != arr[i] :
#                 work += 1
#                 flag = arr[i]
#             arr[i] = 'R'
#         else :
#             flag = arr[i]
#     else :
#         if arr[i] == 'R' :
#             if flag != arr[i] :
#                 work += 1
#                 flag = arr[i]
#             arr[i] = 'B'
#         else :
#             flag = arr[i]
# print(work)

