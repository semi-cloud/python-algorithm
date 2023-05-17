# 리조트 이용하기 위해 지불해야 하는 최소 비용
# 쿠폰을 쓰는 경우 / 안 쓰는 경우로 나누어야함(발급되자마자 사용하는 것이 최솟값 보장 X)
# dp[day][choice] => 쿠폰 개수를 같이 관리할 방법이 X
# 하루 마다 총 네 가지 경우의 수가 존재 (하루 이용권 / 연속 3일 / 연속 5일 / 쿠폰)

# dp[x][y] : 날짜 x에 쿠폰이 y개 있는 경우 최소 비용 (선택을 저장 하지 않아도 됌)
# 인자로 선택을 받아서, day == N일때 각 선택 별로 비용을 반환하도록 했는데 이렇게 하는게 X

def dfs(day, coupon):   # 0원에서 시작
    if day > N: return 0
    if dp[day][coupon] != float("inf"): return dp[day][coupon]

    if visit[day]:   # 갈 수 없는 날인 경우
        dp[day][coupon] = dfs(day + 1, coupon)   # 다음날로 이동
        return dp[day][coupon]

    dp[day][coupon] = min(   # 세 가지 경우의 수에서 최소 비용 계산, 거꾸로 올라오면서 비용이 계산됌
        min(dfs(day + 1, coupon) + 10000, dfs(day + 3, coupon + 1) + 25000),
        dfs(day + 5, coupon + 2) + 37000
    )

    if coupon >= 3:    # 쿠폰을 쓸 수 있다면 써보고, 최소 비용 다시 계산
        dp[day][coupon] = min(dp[day][coupon], dfs(day + 1, coupon - 3))  # 쿠폰을 쓴 만큼 차감, 하루 무료이므로 추가 비용은 X
    return dp[day][coupon]

N, M = map(int, input().split())  # 100
visit = [False for _ in range(N+1)]
dp = [[float("inf") for _ in range(N+1)] for _ in range(N+1)]

if M > 0:
    temp = list(map(int, input().split()))
    for i in range(len(temp)):  # 이용 불가능한 날 표시
        visit[temp[i]] = True

print(dfs(1, 0))
