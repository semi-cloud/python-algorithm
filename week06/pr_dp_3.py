# 오른쪽과 아래쪽으로만 움직여 집에서 학교까지 갈 수 있는 최단경로의 개수 구하기
def solution(m, n, puddles):
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue

            if [j, i] in puddles:   # 웅덩이가 존재하면 건너뛰기
                continue
            else:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007

    return dp[n][m]

n, m = map(int, input().split(' '))
puddles = [list(map(int, input().split(' '))) for _ in range(1)]

# puddles = [[q,p] for [p,q] in puddles]   # 웅덩이 좌표 뒤집기
dp = [[0] * (m+1) for _ in range(n+1)]
dp[1][1] = 1   # 시작 위치
print(solution(m, n, puddles))
