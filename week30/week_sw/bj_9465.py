# 2n개의 스티커 중에서 두 변을 공유 하지 않는 스티커 점수의 최댓 값을 출력
# DP : 1. 규칙 찾기 2. 이전 값이 다음 값에 어떻게 영향을 미치는가

# 50  10 + 30  max(100+30, 100+50+50) => 왼쪽 전 대각선과 전전 대각선 중 어떤 것을 고르느냐에 따라 최대값이 결정됌
# 30  50 + 50  max(70+30+10, 70+50)

T = int(input())
for _ in range(T):
    n = int(input())
    arr = [[] for _ in range(2)]
    for i in range(2):
        arr[i] = list(map(int, input().split()))

    dp = [[0 for _ in range(n)] for _ in range(2)]
    dp[0][0], dp[1][0] = arr[0][0], arr[1][0]

    if n > 1:
        dp[0][1], dp[1][1] = arr[0][1]+arr[1][0], arr[1][1]+arr[0][0]  # 대각선 교차값
        for i in range(2, n):
            dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + arr[0][i]
            dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + arr[1][i]
    print(max(dp[0][n-1], dp[1][n-1]))

