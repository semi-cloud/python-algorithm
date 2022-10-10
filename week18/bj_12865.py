N, K = map(int, input().split())
bag = [[0, 0]]
dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(N):
    bag.append(list(map(int, input().split())))

for i in range(1, N+1):
    for j in range(1, K+1):   # 배낭의 허용 무게
        w = bag[i][0]  # 물건 무게
        v = bag[i][1]  # 물건 가치

        if j >= w:    # 배낭의 허용 무게 보다 넣을 물건의 무게가 더 작은 경우 넣기
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
        else:         # 베낭의 허용 무게 보다 넣을 물건의 무게가 큰 경우 넣지 않음
            dp[i][j] = dp[i-1][j]
print(dp[N][K])

