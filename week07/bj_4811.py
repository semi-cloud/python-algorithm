dp = [[0] * 31 for _ in range(31)]
for j in range(31):
    dp[0][j] = 1

for i in range(31):        # dp 값 미리 채우기
    for j in range(i, 31):  # (i <= j 부분은 x)
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]   # 알약 반개 i번, 알약 한개를 j번 먹었을 때 경우의 수

while True:
    n = int(input())
    if n == 0:
        break
    else:
        print(dp[n][n])




