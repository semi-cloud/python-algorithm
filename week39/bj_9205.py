# 좌표 평면에서의 BFS

from collections import deque

dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
def bfs(a, b):
    q = deque([[a, b]])
    visited = [False for _ in range(n)]

    while q:
        x, y = q.popleft()

        if abs(festival[0] - x) + abs(festival[1] - y) <= 1000:  # 목적지 도달 가능한 경우
            print("happy")
            return True

        for idx in range(n):   # 아 하나씩 해야 하는데
            if visited[idx]: continue  # 이미 방문한 편의점일 경우

            nx, ny = departs[idx][0], departs[idx][1]
            dist = abs(nx - x) + abs(ny - y)  # 거리 비교

            if dist <= 1000:
                visited[idx] = True
                q.append([nx, ny])  # 도달 가능한 편의점 모두 담기

    # 현재 거리가 1000m 보다 먼 경우 맥주 고갈
    print("sad")

t = int(input())
for _ in range(t):
    n = int(input())

    house = list(map(int, input().split(" ")))
    departs = []
    for i in range(n):
        departs.append(list(map(int, input().split(" "))))

    departs.sort(key=lambda x: (x[0], x[1]))  # 편의점 위치 오름 차순 정렬
    festival = list(map(int, input().split(" ")))

    bfs(house[0], house[1])

# 1000 거리 마다 20병 소진, 편의점이 중간에 없다면 갈 수 X
# 도달할 수 있는 경우 : 1000m 마다 편의점이 존재
# 도달할 수 없는 경우 : 1000m 가 넘어갔는데 편의점이 없다면 도달 X
# visit = [[False for _ in range(b)] for _ in range()] 범위 선정이 애매(배열 크기가 정해져 있지 않은 좌표 평면계)
