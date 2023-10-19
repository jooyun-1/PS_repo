N = int(input())

buildings = list(map(int, input().split()))
result = 0
for i1, y1 in enumerate(buildings):
    x1 = i1 + 1
    # 오른쪽
    cur_slope_right = None
    cnt = 0
    for i2 in range(i1+1, N+1):
        if i2 == N:
            break
        x2 = i2 + 1
        y2 = buildings[i2]
        slope_right = (y2 - y1) / (x2 - x1)
        if cur_slope_right is None or cur_slope_right < slope_right:
            cur_slope_right = slope_right
            cnt += 1
    # 왼쪽
    cur_slope_left = None
    for i3 in range(i1-1, -1, -1):
        if i3 == -1:
            break
        x2 = i3 + 1
        y2 = buildings[i3]
        slope_left = (y2 - y1) / (x2 - x1)
        if cur_slope_left is None or cur_slope_left > slope_left:
            cur_slope_left = slope_left
            cnt += 1

    if cnt > result:
        result = cnt

print(result)