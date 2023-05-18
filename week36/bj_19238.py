from collections import deque

N, M, fuel = map(int, input().split())  # 맵 크기, 승객, 연료 양
arr = [list(map(int, input().split())) for _ in range(N)]
tx, ty = map(int, input().split())
end_points = [[list() for _ in range(N)] for _ in range(N)]

dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
def get_passenger(a, b):  # 가장 가까운 손님 찾기(여러 명일 때는 리스트 반환, 나중에 정렬)
    global fuel

    visit = [[False for _ in range(N)] for _ in range(N)]  # 택시가 매번 이동할 때마다 최단 거리를 찾아야 하므로 초기화 필요
    passengers = []
    q = deque([[a, b, 0]])
    visit[a][b] = True
    prev = int(1e9)

    # 1. 택시와 손님 위치가 처음 부터 같은 경우
    while q:
        x, y, cost = q.popleft()  # 위치, 이동 거리
        if arr[x][y] == -1 and x == tx - 1 and y == ty - 1:
            return [[0, x, y]]

        if arr[x][y] == -1:      # 최단 거리 탐색 중에 손님을 만난 경우
            prev = cost
            passengers.append([cost, x, y])  # 최단 거리가 같은 손님 처리 중에 정렬
            continue

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N or arr[nx][ny] == 1: continue

            if prev < cost: continue   # 최단 거리 보다 멀리 있는 승객을 찾으러 갈 필요 X
            if not passengers and fuel < cost: return []   # 현재 가지고 있는 연료 양으로 이동을 못하는 경우

            if not visit[nx][ny]:
                visit[nx][ny] = True
                q.append([nx, ny, cost + 1])
    return passengers

def move(a, b):  # 택시 시작 위치 = 승객 탑승 위치
    global fuel

    visit = [[False for _ in range(N)] for _ in range(N)]  # 택시가 매번 이동할 때마다 최단 거리를 찾아야 하므로 초기화 필요
    q = deque([[a, b, 0]])
    visit[a][b] = True

    while q:
        x, y, cost = q.popleft()  # 위치, 이동 거리
        if x == end_points[a][b][0] and y == end_points[a][b][1]:   # 도착 지점에 도달한 경우
            if fuel < cost: return False  # 목적지 도착 이전에 연료가 바닥이 나는 경우

            fuel -= cost
            fuel += cost * 2
            return True

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N or arr[nx][ny] == 1: continue

            if not visit[nx][ny]:
                visit[nx][ny] = True
                q.append([nx, ny, cost + 1])

for i in range(M):
    sx, sy, ex, ey = map(int, input().split())
    end_points[sx-1][sy-1] = [ex - 1, ey - 1]
    arr[sx-1][sy-1] = -1   # 승객 출발 위치 저장

cnt = 0
start_x, start_y = tx - 1, ty - 1
while cnt < M:
    res = get_passenger(start_x, start_y)  # 1. 가장 가까이 있는 손님을 찾기
    if not res:
        print(-1)
        break
    else:         # 데리러 갈 수 있는 손님이 있는 경우
        res.sort(key=lambda x: (x[0], x[1], x[2]))  # 거리, 행, 열
        dist, x, y = res[0]
        fuel -= dist   # 이동한 만큼 바로 연료 차감

        arr[x][y] = 0     # 승객 제거
        if move(x, y):  # 손님 목적지로 최단 경로로 이동 가능한 경우
            start_x, start_y = end_points[x][y][0], end_points[x][y][1]   # 손님 목적지를 택시 시작 위치로 다시 지정
            cnt += 1
        else:
            print(-1)
            break
else:
    print(fuel)