# 두 문자열에 모두 포함된 가장 긴 공통 부분 문자열을 찾는 프로그램

s1 = input()
s2 = input()
N, M = len(s1), len(s2)
dp = [[0] * (M+1) for _ in range(N+1)]  # `X[0…i-1]`, `Y[0…j-1]`의 LCS 길이를 저장
max_len = 0

for i in range(1, N+1):
    for j in range(1, M+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i - 1][j - 1] + 1    # 대각선에 있는(전 공통 부분 문자열의 최대 길이) 원소 + 1
            max_len = max(max_len, dp[i][j])   # 가장 긴 수 저장

print(max_len)

