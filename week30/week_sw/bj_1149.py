# 양옆에 수와 색이 같으면 안되는 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값 구하기

N = int(input())  # 1000
cost = [0] + [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(3)] for _ in range(N+1)]

dp[1][0], dp[1][1], dp[1][2] = cost[1][0], cost[1][1], cost[1][2]  # 빨, 초, 파
for i in range(2, N+1):
    dp[i][0] = min(cost[i][0] + dp[i-1][1], cost[i][0] + dp[i-1][2])   # 다음 집에 빨강색을 칠하는 최소 값은 앞 집에서 초록과 파란색을 칠하는 수 두 가지중 더한 값이 작은 값
    dp[i][1] = min(cost[i][1] + dp[i-1][0], cost[i][1] + dp[i-1][2])
    dp[i][2] = min(cost[i][2] + dp[i-1][0], cost[i][2] + dp[i-1][1])

print(min(dp[N]))