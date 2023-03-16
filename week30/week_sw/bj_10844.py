# 길이가 N인 계단 수(인접한 모든 자리의 차이가 1)가 총 몇 개 있는지 구하기
# 만들어 놓은 수의 마지막 숫자에 의해서(이전 숫자) 그 다음에 올 수 있는 숫자들의 경우의 수가 정해지게 됌
# dp[i][k] : i 자리 수에서 끝자리가 k 수 일 때 계단 수의 개수

N = int(input())  # 100
dp = [[0 for _ in range(10)] for _ in range(N+1)]
MOD = 1000000000

for i in range(1, 10):  # 한 자리 수인 경우 초기화
    dp[1][i] = 1

for i in range(2, N+1):
    for j in range(10):
        if j == 0:  # 마지막 숫자 값이 0인 경우 이전에 1인 경우의 수 밖에 못옴
            dp[i][j] = dp[i-1][1] % MOD
        elif j == 9:  # 마지막 숫자 값이 9인 경우 이전에 8인 경우의 수 밖에 못옴
            dp[i][j] = dp[i-1][8] % MOD
        else:  # 끝 자리 수가 1-8인 경우 뒤에 2가지 경우의 수가 올 수 있음
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1] % MOD

print(sum(dp[N]) % MOD)

# 1. 시간 초과 코드 : 백트래킹
# def graph(depth, n):
#     global ans
#     if n < 0 or n > 9:  # 한 자리 수만 가능
#         return
#
#     if depth == N:
#         ans += 1
#         return
#
#     graph(depth + 1, n - 1)
#     graph(depth + 1, n + 1)
#
# if N == 1:
#     print(9)
# else:
#     for i in range(1, 10):
#         graph(1, i)
#     print(ans % 1000000000)

