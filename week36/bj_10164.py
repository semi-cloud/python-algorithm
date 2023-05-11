# 로봇 => 오른쪽 / 아래 인접한 칸으로 이동 가능 => 왔던 길을 다시 되돌아가는 경우가 없으므로 방문 배열 필요 X
# 3 X 3 칸에서 왼/오 이동으로만 갈 수 있는 경로는 3개 고정

# 1. 재귀 + 백트래킹 풀이 : 시간 초과
# 시간 줄이는 법 => 해당 위치에서 [N][M] 지점으로 갈 수 있는 경로 개수를 저장(메모지에이션)
import sys
sys.setrecursionlimit(10 ** 7)

def all_dfs(x, y):
    if dp[x][y] > 0: return dp[x][y]

    if x == N - 1 and y == M - 1:
        return 1

    for i in range(2):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
        dp[x][y] += all_dfs(nx, ny)
    return dp[x][y]

def dfs(x, y, o):  # 한 노드당 2개씩 늘어남 => 최대 2^15 => 시간 초과
    if not o and (x > ox or y > oy): return 0  # 백트래킹 가지 치기

    if dp[x][y] > 0: return dp[x][y]
    if o and x == N - 1 and y == M - 1:  # 오른쪽 끝에 o 지점을 지나면서 도달한 경우
        return 1

    for i in range(2):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M: continue

        if nx == ox and ny == oy:  # o 지점을 만난 이후 경로는 모두 True 표시
            dp[x][y] += dfs(nx, ny, True)
        else:            # o 지점을 못 만났다면 False
            dp[x][y] += dfs(nx, ny, o)
    return dp[x][y]

dx, dy = [1, 0], [0, 1]
N, M, K = map(int, input().split())
ox, oy = 0, 0
res = 0
arr = [[0 for _ in range(M)] for _ in range(N)]
dp = [[0 for _ in range(M)] for _ in range(N)]

temp = 1
for i in range(N):
    for j in range(M):
        if temp == K: ox, oy = i, j  # o의 위치 기억
        arr[i][j] = temp
        temp += 1

if K == 0:  # 0 표시가 된 칸이 없는 경우 => 그냥 오른쪽 / 아래 이동 가능한 모든 조합의 수 구하기
    all_dfs(0, 0)
else:
    dfs(0, 0, False)
print(dp[0][0])

# 2. DP 풀이
# dp = [[0 for _ in range(M+1)] for _ in range(N+1)]  # 이렇게 가장자리를 계산해야 하는데 범위를 벗어날 경우, 0으로 한칸을 더 채워줌
# dp[1][1] = 1
# ox, oy = ox + 1, oy + 1
#
# for i in range(1, N+1):
#     for j in range(1, M+1):
#         if i == 1 and j == 1: continue
#
#         if (i > ox and j < oy) or (i < ox and j > oy):  # O 를 기준으로 가로 세로 선을 그었을 때, 왼쪽 아래 + 오른쪽 위는 불가능한 경로 지역
#             dp[i][j] = 0
#         else:
#             dp[i][j] = dp[i-1][j] + dp[i][j-1]
# print(dp[N][M])
