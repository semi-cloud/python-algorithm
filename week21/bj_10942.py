# DP = 점화식이 떠오르지 않는다면 테스트 케이스를 통해 규칙 찾기
# DP[s][e] = s부터 e 위치까지의 숫자의 펠린드롬 여부(맞으면 1, 아니면 0)

import sys
sys.setrecursionlimit(60000)

N = int(input())  # 2,000
arr = list(map(int, sys.stdin.readline().split()))
M = int(input())  # 1,000,000
quest = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
dp = [[-1 for _ in range(N+1)] for _ in range(N+1)]

# 탑 다운(재귀) 사용
def solution(i, j):
    # 종료 조건
    if i > j:  # 범위를 넘어가는 경우
        return 1

    if dp[i][j] > -1:
        return dp[i][j]

    if i == j:      # 길이가 1인 경우는 무조건 성립
        dp[i][j] = 1

    if j - i == 1:  # 길이가 2인 경우
        if arr[i - 1] == arr[j - 1]:  # 두 수가 같은 경우에 펠린드롬 성립
            dp[i][j] = 1
        else:
            dp[i][j] = 0

    if arr[i - 1] == arr[j - 1]:    # 양쪽 끝의 숫자가 같아야 재귀적으로 안쪽의 펠린드롬 여부 탐색
        dp[i][j] = solution(i + 1, j - 1)  # 절반에서 양쪽이 아니라 껍질처럼 안쪽이 펠린드롬을 만족 여부에 따라 똑같이 결정
    else:
        dp[i][j] = 0
    return dp[i][j]        # 매 if문 안에서 리턴하지 않고 여기서 한번만 리턴


for s, e in quest:
    print(solution(s, e))
