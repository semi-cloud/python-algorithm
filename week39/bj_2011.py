# BEAN -> 25114 -> (25)(1)(1)(4) / (2)(5)(11)(4) / (25)(11)(4) 등 여러 가지 경우의 수 존재
# 괄호를 치는 방식 개수 구하기 => dp[i][j] = 문자열 i-j 위치의 숫자에서 나올 수 있는 경우의 수 (X)
# dp[i] : i 번째 위치 까지 만들어 낼 수 있는 단어 종류 개수 (O)

p = input()  # 5000
N = len(p)

if p[0] == '0':     # 암호가 잘못 되어 암호를 해석할 수 없는 경우
    print(0)
else:
    p = " " + p
    mod = 1000000
    dp = [0 for _ in range(N+1)]
    dp[0], dp[1] = 1, 1

    for i in range(2, N+1):
        if 1 <= int(p[i]) <= 9:    # 1. 한 자리 숫자로 보는 경우
            dp[i] = (dp[i] + dp[i-1]) % mod   # 바로 이전까지의 경우의 수 가져와서 더하기

        if 10 <= int(p[i-1]) * 10 + int(p[i]) <= 26:   # 2. 두 자리 숫자로 보는 경우
            dp[i] = (dp[i] + dp[i-2]) % mod  # 2번째 이전까지의 경우의 수 가져와서 더하기

    print(dp[N])


# def top_down(i, j):
#     s, e = int(p[i]), int(p[j])
#     if dp[s][e]: return dp[s][e]
#
#     if i == j: return 1  # 한 자리 까지 떨어지는 경우
#
#     num = int(p[i:j+1])
#     if 0 > num or 26 < num: return 0    # 해당 범위에 속하는 숫자가 알파벳 범위인 경우가 아니면
#
#     mid = (i + j) // 2
#     l_cnt = top_down(i, mid)     # 1
#     r_cnt = top_down(mid + 1, j)   # 3
#     return l_cnt * r_cnt
