# 오름차순을 이루는 개수 구하기(같아도 가능)

N = int(input())
dp = [[0 for _ in range(10)] for _ in range(N+1)]

for i in range(10):  # 초기값 갱신
    dp[1][i] = 1

for i in range(2, N+1):
    for j in range(10):
        for k in range(j, 10):
            dp[i][j] += dp[i-1][k]
            dp[i][j] %= 10007   # 오버플로우 방지(부호 비트로 인해 양수 + 양수 = 음수)

        # for k in range(dp[i-1][j], 0, -1): => 220 + 219... (X)
        #     dp[i][j] += k

print(sum(dp[N]) % 10007)
