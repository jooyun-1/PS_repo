def solution(arrows):
    #    위 북동 오른 남동 아래 남서 왼 북서 
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]

    x, y = 0, 0
    # 중복을 없애기 위해 set으로 설정
    visited_node = set()
    visited_node.add((x,y))
    route = set()
    cycle = 0
    for arrow in arrows:
        # 모래시계 교차점을 정점으로 만들기 위해 두칸 이동
        for _ in range(2):
            nx, ny = x+dx[arrow], y + dy[arrow]
            if (nx,ny) in visited_node and (x, y, nx, ny) not in route:
                cycle += 1
            # 엣지 추가 (왔다갔다 경로를 이용)
            route.add((x,y, nx, ny))
            route.add((nx, ny, x,y))
            # 노드 추가
            visited_node.add((nx, ny))
            x, y = nx, ny
    return cycle