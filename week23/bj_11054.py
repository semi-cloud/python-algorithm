# 수열의 부분 수열 중 바이토닉 수열이면서 가장 긴 수열의 길이를 구하기

N = int(input())
arr = list(map(int, input().split()))
increase_dp = [1 for _ in range(N)]
decrease_dp = [1 for _ in range(N)]

# 1. 모든 원소들의 증가하는 부분 수열의 크기 : 순방향 탐색
for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            increase_dp[i] = max(increase_dp[i], increase_dp[j] + 1)

# 2. 모든 원소들의 감소하는 부분 수열의 크기 : 역방향 탐색
for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if arr[i] > arr[j]:
            decrease_dp[i] = max(decrease_dp[i], decrease_dp[j] + 1)

# 3. 각 인덱스별로 증가하는 수열 길이 + 감소하는 수열 길이의 합이 가장 큰 지점이 최대 크기
sum = 0
for i in range(N):
    sum = max(sum, increase_dp[i] + decrease_dp[i])
print(sum-1)  # 겹치는 부분 제거
