# 큐로 했다면, 방문 처리를 하지 못해 다시 되돌아오면서 꼬여버림
# 첫번째 도착점에 도달 하는게 무조건 최소가 되도록 해야함 => 우선순위 큐 사용
# 우선순위 큐 조건 : 해당 위치 까지 가장 최소 거울을 가진 지점(경로) 을 뽑기 때문에 최소값임이 보장 가능(다익스트라)

from heapq import heappop, heappush

dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
def bfs(a, b):
    hq = []
    for i in range(4):
        heappush(hq, [0, a, b, i])
    cost[a][b] = 0

    while hq:
        cnt, x, y, dir = heappop(hq)
        if (x != a or y != b) and arr[x][y] == "C":   # 매번 가장 최소 거울을 사용하는 경로를 뽑음
            return cnt          # 가장 먼저 도달 하는 경로가 최소값임이 보장이 됌

        if cost[x][y] < cnt:  # 기존 저장 되어 있던 최소 값보다 큰 경우 탐색할 필요가 X
            continue          # 이미 최단 경로가 정해진 곳은 다시 방문하지 X

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= H or ny < 0 or ny >= W or arr[nx][ny] == '*' or visit[nx][ny][dir][i]:  # 똑같은 위치에서 거울을 더 사용하는 경로라면 스탑
                continue

            if (x == a and y == b) or dir == i:  # 이전 방향하고 같은 경우 그대로 유지
                mirror_cnt = cnt
            else:               # 이전 방향하고 달라지면 꺽인 부분이므로 거울 개수 추가
                mirror_cnt = cnt + 1

            visit[nx][ny][dir][i] = True  # 가는 경로 막기
            cost[nx][ny] = min(cost[nx][ny], mirror_cnt)  # 매 번 거울 횟소 최소값을 갱신(똑같은 위치라도 사용해야 하는 거울 개수가 달라짐)
            heappush(hq, [mirror_cnt, nx, ny, i])

W, H = map(int, input().split(" "))  # 100
arr = [[0 for _ in range(W)] for _ in range(H)]
s, e = 0, 0

for i in range(H):
    temp = list(input())
    for j in range(W):
        if temp[j] == "C":
            s, e = i, j
        arr[i][j] = temp[j]

cost = [[int(1e9) for _ in range(W)] for _ in range(H)]  # 방문 + 최소 횟수 갱신
# 3차원이 아닌 4차원 방문 배열: 이전에서 온 방향 + 다음 가려는 방향 모두 기록 필수
visit = [[[[False for _ in range(4)] for _ in range(4)] for _ in range(W)] for _ in range(H)]
print(bfs(s, e))

# q = deque([[a, b, 0, 0]])
# visit[a][b] = [[True for _ in range(4)] for _ in range(4)]
# cost[a][b] = 0
# while q:
#     x, y, dir, cnt = q.popleft()
