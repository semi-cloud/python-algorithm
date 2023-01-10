# 3×N 크기의 벽을 2×1, 1×2 크기의 타일로 채우는 경우의 수

# 미리 경우의 수를 구해보고 수를 토대로 점화식을 도출해내는 방식
# dp[N] : 가로 길이가 N일때 타일을 붙일 수 있는 경우의 수
# dp[2] : 3
# dp[4] : dp[2(4-2)] * dp[2(4-2)] + 2(특수한 모양)
# dp[6] : dp[4] * dp[2] + dp[2] * 2(dp[4]일때의 특수 모양 2가지) + 2
# dp[8] : dp[6] * dp[2] + dp[4] * 2 + dp[2] * 2 + dp[0] * 2
# dp[10] : dp[8] * dp[2] + dp[6] * 2 + dp[4] * 2 + dp[2] * 2 + dp[0] * 2
# dp[N] : dp[N-2] * dp[2] + dp[N-4] * 2 + ... + dp[0] * 2
# 왼쪽이 아니라 오른쪽 부분의 특이 케이스들도 고려해줘야 하기 떄문에 각 부분에 *2

N = int(input())
dp = [0 for _ in range(N+1)]
dp[0] = 1

if N >= 2:   # N = 1일때 인데스 에러 방지
    dp[2] = 3

for i in range(4, N+1, 2):     # 짝수일 때만 모든 타일을 채울 수 있음
    dp[i] += dp[i-2] * 3       # dp[i-2] * dp[2]
    for j in range(i, -1, -2):  # 가로 길이가 i일때 특이 케이스
        dp[i] += dp[j-4] * 2

print(dp[N])


# 시간 초과 브루트 포스 코드
# 메모제이션(DP)을 어디에 적용할 수 있을까?
# def get_attach_pos(copy):
#     x, y = -1, -1
#     for i in range(3):  # 타일을 붙일 수 있는 위치 찾기
#         for j in range(N):
#             if copy[i][j] == 0:
#                 return i, j
#     return x, y
#
# cnt = 0
# def solution(copy):
#     global cnt
#
#     x, y = get_attach_pos(copy)
#     if x == -1 and y == -1:   # 타일을 다 붙였다면 종료
#         cnt += 1
#         return
#
#     for k in range(2):    # 1x2 타일, 2x1 타일 경우의 수
#         nx, ny = x + dx[k], y + dy[k]
#
#         if 0 <= nx < 3 and 0 <= ny < N and copy[nx][ny] == 0:  # 범위 내에 있고 아직 방문하지 않았다면
#             copy[x][y], copy[nx][ny] = k + 1, k + 1
#             solution(copy)
#             copy[x][y], copy[nx][ny] = 0, 0
#
# N = int(input())
# arr = [[0 for _ in range(N)] for _ in range(3)]
# dx, dy = [1, 0], [0, 1]     # 아래, 오른쪽
# solution(arr)
# print(cnt)
# 만약 위치를 찾는 이중 포문 안에 타일을 붙이는 경우의 수 반복문을 넣는다면
# 타일을 다 붙인 이후 돌아올 때 범위를 넘어가서 타일을 못 붙힌 다면 종료가 아니라 다음 노드에서 재귀가 또 시작하므로, 빈 공간까지 생성