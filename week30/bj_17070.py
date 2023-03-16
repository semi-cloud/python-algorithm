# 파이프 미는 방향 및 45도 회전으로 가능한 결과 방향 :  →, ↘, ↓ 세가지 경우만 가능
# 파이프의 한쪽 끝을 (1, 1) (1,2) 가로 방향에서 (N, N)로 이동시키는 방법의 개수 구하기
# 이전이 어떤 모양을 했느냐에 따라 영향을 받으므로 DP 가능할듯
# 미리 어느 위치까지 이동시키는 방법의 개수를 저장해 두면 다른 경로를 찾을 때도 메모지에이션 가능
# 한 번 갔던 곳의 DFS 결과 값을 저장해두고 나중에 이 곳에 다시 방문하면 또 탐색하지 말고 이 값을 재사용

# 1. DFS + 메모제이션
def dfs(x, y, dir):  # 길이가 2인 파이프의 위치
    if x == N-1 and y == N-1:  # 끝 점에 도달했다면 경우의 수 증가시키기
        return 1

    if dp[x][y][dir] != -1:   # 가는 경로 개수가 이미 계산 되어 있다면 다시 재귀 돌릴 필요 없이
        return dp[x][y][dir]  # 해당 위치의 경로 개수 값 반환

    dp[x][y][dir] = 0   # 0으로 초기화 안해주면 더할 때 값에 오류가 생김
    i, j = 0, 0
    if dir == 1:        # 1. 이전 모양이 대각선인 경우
        i, j = 0, 2
    elif dir == 0:      # 2. 이전 모양이 가로인 경우
        i, j = 0, 1
    elif dir == 2:      # 3. 이전 모양이 세로인 경우
        i, j = 1, 2

    for idx in range(i, j+1):
        nx, ny = x + dx[idx], y + dy[idx]

        if nx < 0 or nx >= N or ny < 0 or ny >= N or arr[nx][ny] == 1: continue  # 이동 방향에 벽이 존재하면 파이프 이동 불가능
        if idx == 1 and (arr[nx-1][ny] == 1 or arr[nx][ny-1] == 1): continue  # 대각선으로 이동하려 할 때 가로와 세로에 벽이 있다변 불가능

        dp[x][y][dir] += dfs(nx, ny, idx)  # 다음의 결과 값을 이전 dp 값이랑 더해서 저장 해야함(그냥 =으로 대입하면 X)
    return dp[x][y][dir]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]   # 벽이 1(파이프는 0만 지날 수 있음)
dp = [[[-1 for _ in range(3)] for _ in range(N)] for _ in range(N)]  # dp[x][y][k] : arr[x][y] 에서 k 번째 방향의 경우의 수
dx, dy = [0, 1, 1], [1, 1, 0]  # 가로, 대각선, 세로
print(dfs(0, 1, 0))

# 2. DP + 바텀 업