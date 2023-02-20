# 위 -> 아래 내려올 때 선택된 수의 합이 최대가 되는 경로
# 맨 왼쪽의 노드 : 오른쪽 대각선 경로만 존재, 가운데 노드 : max(왼쪽 대각선, 오른쪽 대각선), 맨 오른쪽 노드 : 왼쪽 대각선 경로만 존재

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(i)] for i in range(1, n+1)]

dp[0][0] = arr[0][0]
for i in range(1, n):
    for j in range(i+1):
        if j == 0:    # 1. 왼쪽 노드
            dp[i][j] = arr[i][j] + dp[i-1][j]
        elif i == j:  # 2. 오른쪽 노드
            dp[i][j] = arr[i][j] + dp[i-1][j-1]
        else:         # 3. 가운데 노드
            dp[i][j] = arr[i][j] + max(dp[i-1][j-1], dp[i-1][j])
print(max(dp[n-1]))   # 삼각형 맨 아래 줄에서 최대 경로의 값 찾기







