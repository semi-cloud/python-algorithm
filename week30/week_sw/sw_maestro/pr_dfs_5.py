# 2번 유사 문제

from collections import deque

def bfs(a, b, s, e, arr):
    dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
    q = deque([(a, b, 0)])
    arr[a][b] = 0  # 시작 위치를 0부터 시작

    while q:
        x, y, d = q.popleft()
        if x == s and y == e:  # 먼저 목표 지점에 도달한 것이 최단 거리
            return d // 2  # 좌표를 2배 했으니 실제 거리는 반

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < 101 and 0 <= ny < 101 and arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx, ny, d + 1))


def solution(rectangle, characterX, characterY, itemX, itemY):
    arr = [[0 for _ in range(101)] for _ in range(101)]  # 좌표 두배
    # 1. 1로 모든 면적을 표시
    for x1, y1, x2, y2 in rectangle:
        for i in range(2 * x1, (2 * x2) + 1):
            for j in range(2 * y1, (2 * y2) + 1):
                arr[i][j] = 1

    # 2. 주어진 좌표를 한 칸씩 줄여서 내부를 비우고 변만 남기기
    for x1, y1, x2, y2 in rectangle:
        for i in range(2 * x1 + 1, 2 * x2):
            for j in range(2 * y1 + 1, 2 * y2):
                arr[i][j] = 0

    return bfs(2 * characterX, 2 * characterY, 2 * itemX, 2 * itemY, arr)
