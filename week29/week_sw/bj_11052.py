# N개의 카드를 구매하기 위해 민규가 지불해야 하는 금액의 최댓값

N = int(input())
money = [0] + list(map(int, input().split()))
dp = [0 for _ in range(N+1)]   # i개 카드를 구매했을 떄 최대값

for i in range(1, N+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], money[j] + dp[i-j])   # 이전의 카드를 지불한 최대 금액 + 현재 카드팩 가격 중 최대값 비교

print(dp[N])

# for i in range(1, N+1):
#     for j in range(i):
#         dp[i] = max(dp[i], dp[j] + money[i-j])




