# 원숭이가 최소한의 동작으로 시작지점에서 도착지점까지 갈 수 있는 방법을 알아내는 프로그램(최소)
# 주의 : k 번을 무조건 사용 해야 하는 것이 X, 다 사용 안할 수도 있고 원숭이 -> 말 -> 원숭이 -> 말 이렇게 움직이기도 가능
# BFS + 완전 탐색

# 기존에 16개 방향을 체크 했을 때 방문 체크를 하면 안됬던 것과 달리(가는 길까지 체크 해 버려서) 마지막 지점만 방문 체크가 됌
# 방문 체크가 필요 : 가려고 하는 곳에 이미 방문이 되었다는 것은 먼저 방문한 놈이 빠르므로 최소 경로가 정해졌다는 것 = 뒤에서 오는 후발 주자들은 그 이후의 길을 체크할 필요가 X
# 둘의 경우의 수에 움직일 수 있는 말의 경우 값을 분리 하지 않으면 => 테케 통과 X(이미 다른 경우의 수에서 k가 차감) -> 큐에 k 값을 넣어서 따로 관리

# 원숭이의 움직임으로 먼저 가다가 아래에서 말의 움직임으로 장애물을 건너뛰는 반례 : 6 / 오답 : -1
# 1
# 5 5
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 1 1
# 0 0 0 1 0

from collections import deque

def move_horse(x, y, cnt, q, dist):
    for i in range(8):   # 8개의 모든 방향 체크(방문 체크 필요)
        nx, ny = x + ddx[i], y + ddy[i]
        if 0 > nx or nx >= H or 0 > ny or ny >= W or arr[nx][ny] == 1 or visit[nx][ny][cnt+1]:  # visit[nx][ny][cnt] : 원숭이로 가는 움직임 까지 막아 버림
            continue

        visit[nx][ny][cnt+1] = True
        q.append((nx, ny, dist + 1, cnt + 1))

def move_monkey(x, y, cnt, q, dist):
    for i in range(4):   # 말 이동 방향이 아닌 상하좌우 이동(방문 체크 필요)
        nx, ny = x + dx[i], y + dy[i]
        if 0 > nx or nx >= H or 0 > ny or ny >= W or arr[nx][ny] == 1 or visit[nx][ny][cnt]:
            continue

        visit[nx][ny][cnt] = True
        q.append((nx, ny, dist + 1, cnt))

def bfs(a, b):
    global k, W, H, res
    q = deque([(a, b, 0, 0)])
    visit[a][b][0] = True  # 시작 지점 방문 체크

    while q:
        x, y, dist, cnt = q.popleft()
        if x == H-1 and y == W-1:
            return dist

        if cnt < k:     # 말로 이동할 수 있는 횟수가 남았다면 말 + 원숭이 경우의 수 체크
            move_horse(x, y, cnt, q, dist)
            move_monkey(x, y, cnt, q, dist)
        else:           # 말로 이동할 수 있는 횟수를 소진 했다면 원숭이 이동 경우의 수만 체크
            move_monkey(x, y, cnt, q, dist)
        print(q)
    return -1

k = int(input())   # 30
W, H = map(int, input().split())  # 200
arr = [list(map(int, input().split())) for _ in range(H)]
res = int(1e9)
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
ddx, ddy = [1, 1, -1, -1, 2, 2, -2, -2], [-2, 2, -2, 2, 1, -1, 1, -1]   # 상 좌 좌 : x 좌표 + 1, y 좌표 -2
visit = [[[False for _ in range(k+1)] for _ in range(W)] for _ in
         range(H)]  # visit[x][y][dir] 가 아니라 visit[x][y][k] : 말 처럼 k 번 움직여서 x,y 좌표에 접근 하였는가?
print(bfs(0, 0))

# dir = {0: [-1, 0], 1: [1, 0], 2: [0, -1], 3: [0, 1]}  # 상 하 좌 우
# horse_dir = [[0, 2, 2], [0, 3, 3], [1, 2, 2], [1, 3, 3], [2, 0, 0], [2, 1, 1], [3, 0, 0], [3, 1, 1],
#              [0, 0, 2], [0, 0, 3], [1, 1, 2], [1, 1, 3], [2, 2, 0], [2, 2, 1], [3, 3, 0], [3, 3, 1]]


