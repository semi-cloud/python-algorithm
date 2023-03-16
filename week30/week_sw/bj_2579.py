# 계단 오르기 게임에서 얻을 수 있는 총 점수의 최댓값 구하기
# 연속된 계단의 경우의 수가 포함 되었을 수 있기 때문에 dp[i-1] 이 아닌 cost[i-1] + dp[i-3]

N = int(input())
cost = [0] + [int(input()) for _ in range(N)]
dp = [0 for _ in range(N+1)]

if N > 1:
    dp[1], dp[2] = cost[1], cost[1] + cost[2]  # 초기값 갱신
    for i in range(3, N+1):
        dp[i] = max(dp[i-3] + cost[i-1] + cost[i], dp[i-2] + cost[i])
    print(dp[N])
else:
    print(cost[1])
