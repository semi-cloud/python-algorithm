# 모든 SCV를 파괴하기 위해 공격해야 하는 횟수의 최솟값
# 한 번에 세개 동시에 공격 가능(9 -> 3 -> 1)

# 2. DFS 로 탐색, 메모지에이션 적용
def dfs(depth, a, b, c):
    global res

    if a <= 0 and b <= 0 and c <= 0:   # 체력이 모두 소진되는 경우 바로 종료(최소값)
        res = min(res, depth)
        return

    if a < 0: a = 0     # 음수 인덱스 방지
    if b < 0: b = 0
    if c < 0: c = 0

    if dp[a][b][c] != int(1e9) and depth >= dp[a][b][c]:  # 이미 값이 초기화가 된 경우
        return   # 더 늦게 같은 값에 도착한 경우 더 탐색할 필요 X

    dp[a][b][c] = depth
    dfs(depth + 1, a - 9, b - 3, c - 1)
    dfs(depth + 1, a - 9, b - 1, c - 3)
    dfs(depth + 1, a - 3, b - 9, c - 1)
    dfs(depth + 1, a - 3, b - 1, c - 9)
    dfs(depth + 1, a - 1, b - 9, c - 3)
    dfs(depth + 1, a - 1, b - 3, c - 9)

    # dp[a][b][c] = min(dp[a][b][c], dfs(depth + 1, a - 9, b - 3, c - 1))
    # dp[a][b][c] = min(dp[a][b][c], dfs(depth + 1, a - 9, b - 1, c - 3))
    # dp[a][b][c] = min(dp[a][b][c], dfs(depth + 1, a - 3, b - 1, c - 9))
    # dp[a][b][c] = min(dp[a][b][c], dfs(depth + 1, a - 3, b - 9, c - 1))
    # dp[a][b][c] = min(dp[a][b][c], dfs(depth + 1, a - 1, b - 3, c - 9))
    # dp[a][b][c] = min(dp[a][b][c], dfs(depth + 1, a - 1, b - 9, c - 3))


N = int(input())  # 3
arr = list(map(int, input().split(" ")))   # 체력이 k 인 SCV를 파괴하는 최소 횟수
dp = [[[int(1e9) for _ in range(61)] for _ in range(61)] for _ in range(61)]
res = float("inf")

for i in range(3 - N):
    arr.append(0)

dfs(0, arr[0], arr[1], arr[2])
print(res)


# 메모리 초과(BFS)
# def bfs():
#     q = deque([[0, arr]])
#
#     while q:
#         depth, scv = q.popleft()
#
#         for i in range(len(scv)):    # 체력이 모두 소진되는 경우 바로 종료(최소값)
#             if scv[i] > 0: break
#         else:
#             return depth
#
#         q.append([depth + 1, [scv[0] - 9, scv[1] - 3, scv[2] - 1]])
#         q.append([depth + 1, [scv[0] - 9, scv[1] - 1, scv[2] - 3]])
#         q.append([depth + 1, [scv[0] - 3, scv[1] - 9, scv[2] - 1]])
#         q.append([depth + 1, [scv[0] - 3, scv[1] - 1, scv[2] - 9]])
#         q.append([depth + 1, [scv[0] - 1, scv[1] - 9, scv[2] - 3]])
#         q.append([depth + 1, [scv[0] - 1, scv[1] - 3, scv[2] - 9]])



