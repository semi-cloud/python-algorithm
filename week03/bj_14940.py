# 지도가 주어 지면 모든 지점에 대해서 목표 지점 까지의 거리 출력

from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
result = [[0] * m for _ in range(n)]
visit = [[False] * m for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def find_target():
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                return i, j


def bfs(a, b):
    arr[a][b] = 0
    queue = deque()
    queue.append((a, b))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if not visit[nx][ny] and arr[nx][ny] == 1:
                visit[nx][ny] = True
                queue.append((nx, ny))
                result[nx][ny] = result[x][y] + 1


start, end = find_target()
bfs(start, end)

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and result[i][j] == 0:
            result[i][j] = -1

for i in range(n):
    print(" ".join(map(str, result[i])))
