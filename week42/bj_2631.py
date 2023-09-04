# 옮겨지는 학생의 수 최소를 구하려면, 옮기지 않아도 되는(오름차순으로 증가) 부분 수열의 최대 길이를 구하기
# 3 7 5 2 6 1 4 에서 최장 증가 부분 수열은 {3, 5, 6} => 7, 2, 1, 4번 학생만 옮기면 됌

N = int(input())  # 200
arr = [int(input()) for _ in range(N)]
dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):   # 현재 위치 보다 왼쪽에 있는 값들중 작은 수들 찾기
        if arr[j] < arr[i]:  # 작은 수들에 대해서 증가하는 부분 수열 최대 길이 갱신
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))
