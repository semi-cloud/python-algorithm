# 도둑루피 크기만큼 소지금을 읽는데, 이때 잃을 수 밖에 없는 최소 금액

from heapq import heappop, heappush

dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
def dijkstra(a, b):
    hq = []
    dist = [[int(1e9) for _ in range(N)] for _ in range(N)]  # 기록을 해놔야 최소값 안되는 경로 가지치기 가능
    heappush(hq, [arr[a][b], a, b])
    dist[a][b] = arr[a][b]

    while hq:
        cost, x, y = heappop(hq)
        if x == N-1 and y == N-1:  # 우선순위 큐 덕분에 가장 먼저 도착 최솟값 보장
            return cost

        if cost > dist[x][y]:      # 본인 경로가 비용이 더 높다면 탐색 X
            continue

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N: continue

            new_cost = dist[x][y] + arr[nx][ny]
            if new_cost < dist[nx][ny]:       # 더 작은 비용의 경로일 경우 갱신 필요
                dist[nx][ny] = new_cost
                heappush(hq, [new_cost, nx, ny])

idx = 1
while True:
    N = int(input())  # 동굴 크기
    if N == 0: break

    arr = [list(map(int, input().split(" "))) for _ in range(N)]
    res = dijkstra(0, 0)
    print("Problem", idx, end="")
    print(":", res)
    idx += 1


