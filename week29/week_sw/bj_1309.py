# 인접하게 배치 불가능 할 때 사자를 배치하는 경우의 수 구하기
# 완전 탐색 + 그래프 탐색(백트래킹)의 경우에는 시간 초과(200,000 * 200,000) => DP 이용
# 결국 N에 비례 해서 추가 되는 거는 1x2 타일 => (o,x) (x,o) (o o) 세 가지 경우로 나누어서 다음에 어떤 것들이 올 수 있는지 탐색

# 현재 o x 추가 -> 이전이 x o / x x (2) : dp[i][0] = dp[i-1][1] + dp[i-1][2]
# 현재 x o 추가 -> 이전이 o x / x x (2) : dp[i][1] = dp[i-1][0] + dp[i-1][2]
# 현재 x x 추가 -> 이전이 x o / o x / x x (3) : dp[i][2] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2]

N = int(input())  # 세로 길이 100,000
dp = [[0 for _ in range(3)] for _ in range(N+1)]

dp[1][0], dp[1][1], dp[1][2] = 1, 1, 1
for i in range(2, N+1):
    dp[i][0] = (dp[i - 1][1] + dp[i - 1][2]) % 9901
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % 9901
    dp[i][2] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % 9901  # 나머지 값을 저장 해야 한다는 점에 주의

print((dp[N][0] + dp[N][1] + dp[N][2]) % 9901)  # 이전에 계산한 값들을 참고해서 아무것도 X + 왼쪽만 + 오른쪽만 모두 더하면 답
