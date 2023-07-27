# 특정 일에 상담을 하면 이후 N일 동안 못하기 때문에 이전 결과가 이후 결과에 영향을 줌
# dp[i] : i일 차에 상담을 했을 때 얻을 수 있는 최대 수익

N = int(input())  # 1,500,000
arr = [list(map(int, input().split(" "))) for _ in range(N)]
dp = [0 for i in range(N+1)]
res, max_val = 0, 0

for i in range(N):
    t, p = arr[i][0], arr[i][1]
    max_val = max(max_val, dp[i])

    if i + t > N:  # 범위를 벗어나는 경우(N+1일째 에는 회사에 없음)
        continue

    dp[i + t] = max(dp[i + t], p + max_val)   # max(기존 값, 현재 까지 최대 이윤 + 현재 이윤)
    # dp[i + t] = max(dp[i + t], p + dp[i])   # 이렇게 하면 X

# [0, 0, 0, 0, 0, 50, 60, 0, 80, 0, 30] : + max_val
# [0, 0, 0, 0, 0, 50, 60, 0, 80, 0, 90] : + dp[i]

