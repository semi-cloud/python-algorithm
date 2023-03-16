# DP = 배열 탐색 한번으로 끝내기 = O(N^2) = 1000,000
# 정사각형 조건 = 왼쪽 위 대각선, 위쪽, 왼쪽이 모두 1 / 정사각형 될 수 없는 조건 : 세 방향에서 하나라도 0 이 존재하는 경우(min 으로 판별)

import math

def solution(board):
    R, C = len(board), len(board[0])

    for i in range(1, R):
        for j in range(1, C):
            if board[i][j] == 0:
                continue
            board[i][j] = min(board[i - 1][j - 1], board[i - 1][j], board[i][j - 1]) + 1

    return math.pow(max(map(max, board)), 2)

#     dp = [[0 for _ in range(C+1)] for _ in range(R+1)]
#     for i in range(R):
#         for j in range(C):
#             nx, ny = i - 1, j - 1
#             if nx < 0 or nx >= R or ny < 0 or ny >= C or board[i][j] == 0:
#                 continue

#             res = min(board[nx][ny], board[nx][j], board[i][ny])
#             if res == 1:      # 세 변 모두 1이고 왼쪽 대각선 위치에 dp 값이 1 이상인 경우
#                 if dp[nx][ny] >= 1:
#                     dp[i][j] = dp[nx][ny] + 1    # 정사각형 확장
#                 else:
#                     dp[i][j] = 1    # 왼쪽 대각선이 0 이면 그냥 1

#     return math.pow(max(map(max, dp)), 2)
