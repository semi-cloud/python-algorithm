# 0부터 N 까지의 정수 K개를 더해서 그 합이 N이 되는 경우의 수 구하기
n, k = map(int, input().split())
dp = [[0] * 201 for _ in range(201)]

# k = 1 일때 : 모든 n에 대해 경우의 수는 자기 자신 하나
# k = 2 일때 : n + 1개 ex) n=3 (1,2)(0,3)(3,0)(2,1), n=4 (1,3)(2,2)(0,4)(3,1)(4,0)
for i in range(201):
    dp[1][i] = 1
    dp[2][i] = i + 1

for i in range(2, 201):    # k
    dp[i][1] = i            # 합이 1이 되는 경우는 k개 ex n=3 (1,0,0)(0,1,0)(0,0,1)
    for j in range(2, 201):    # j
        dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % (10 ** 9)   # 좌측 값 + 상위 값 = 현재 값

print(dp[k][n])



