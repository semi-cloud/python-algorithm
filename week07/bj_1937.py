# 판다가 이동할 수 있는 칸의 수의 최댓값 구하기
import sys

sys.setrecursionlimit(10 ** 6)
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
d = [(0, -1), (-1, 0), (0, 1), (1, 0)]
dp = [[0] * (n+1) for _ in range(n+1)]


def dfs(x, y):
    if dp[x][y] != 0:     # 이미 살 수 있는 최대값을 구해놨다면 그냥 리턴
        return dp[x][y]

    dp[x][y] = 1            # 최소 하루는 살 수 있음
    for dx, dy in d:
        nx, ny = x + dx, y + dy

        if 0 <= nx < n and 0 <= ny < n and arr[x][y] < arr[nx][ny]:    # 이동 가능한 경로면
            dp[x][y] = max(dfs(nx, ny) + 1, dp[x][y])          # (x,y)에서 살 수 있는 최대 일수 저장
    return dp[x][y]


result = 0
for i in range(n):
    for j in range(n):
        result = max(result, dfs(i, j))      # 모든 노드를 시작으로 탐색하면서 최댓값 저장
print(result)