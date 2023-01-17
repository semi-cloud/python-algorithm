# 연구소의 바이러스 M개를 활성 상태로 변경하고자 할때, 모든 빈 칸에 바이러스를 퍼뜨리는 최소 시간 구하기

from collections import deque
from itertools import combinations

def bfs(active):
    q = deque()
    copy = [[-1 for _ in range(N)] for _ in range(N)]  # copy[i][j] != -1인 원소는 방문 되었다고 가정
    max_v = 0

    for x, y in active:    # 활성 바이러스 목록
        q.append((x, y))
        copy[x][y] = 0   # 밑에 비활성 바이러스랑 구분하기 위해 미리 방문처리

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and copy[nx][ny] == -1:
                if arr[nx][ny] == 2:     # 비 활성화 바이러스에 도달했을 경우 활성화 바이러스로 변경
                    q.append((nx, ny))
                    copy[nx][ny] = copy[x][y] + 1
                elif arr[nx][ny] == 0:   # 벽이 아닌 곳으로 이동 하는 경로
                    q.append((nx, ny))
                    copy[nx][ny] = copy[x][y] + 1
                    max_v = max(max_v, copy[nx][ny])

    # 바이러스를 어떠한 조합에서도 모든 빈칸에 퍼트릴 수 없을때
    if wall != list(sum(copy, [])).count(-1):  # -1의 개수가 벽의 개수와 다른 경우
        return (N * N) + 1      # 하나라도 가능하다면 -1을 출력했을 때 답이 min으로 인해 -1이 출력되므로 X, 최댓값으로 설정
    return max_v


N, M = map(int, input().split())  # M : 놓을 수 있는 바이러스의 개수!! 아 이렇게 되면 조합이 가능해짐(나는 2의 개수 == M이라고 생각)
virus = []
arr = [[0 for _ in range(N)] for _ in range(N)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
wall = 0

for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        arr[i][j] = temp[j]
        if temp[j] == 2:
            virus.append((i, j))  # 바이러스 위치
        elif temp[j] == 1:
            wall += 1             # 벽의 개수

result = float("inf")
for comb in combinations(virus, M):
    result = min(result, bfs(comb))   # 각 바이러스 조합에 대한 탐색 시간의 최솟값
print(result if result <= N * N else -1)


