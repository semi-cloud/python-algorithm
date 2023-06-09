# 감소하지 않는 수열 => 맨 왼쪽 행을 제외한 모든 애벌레는 맨 위쪽 행의 증가도와 같아짐
import sys
input = sys.stdin.readline

M, N = map(int, input().split())   # 크기(700), 날짜(1,000,000)
dx, dy = [0, -1, -1], [-1, -1, 0]  # 왼쪽(L), 왼쪽 위(D), 위쪽(U)
arr = [[0 for _ in range(M)] for _ in range(M)]  # 현재 양, 자란 양
grow = [0 for _ in range(2*M-1)]

for _ in range(N):
    zero, one, two = map(int, input().split())
    one += zero
    two += one
    for i in range(zero, one):
        grow[i] += 1
    for i in range(one, two):
        grow[i] += 2

# 1. 왼쪽 / 오른쪽 열에 있는 애벌레 자라기
for i in range(M-1, -1, -1):  # 맨 왼쪽 열
    arr[i][0] += grow[M - i - 1]

for i in range(1, M):     # 맨 위쪽 행
    arr[0][i] += grow[M + i - 1]

# 2. 두번째 행 / 열 증가도 처리
for i in range(1, M):  # 두 번째 행
    for j in range(1, M):  # 두 번째 열
        if i != 1 and j != 1: continue
        max_grow = 0
        for k in range(3):
            nx, ny = i + dx[k], j + dy[k]
            max_grow = max(max_grow, arr[nx][ny])
        arr[i][j] += max_grow

for j in range(2, M):
    plus = arr[1][j]
    for i in range(2, M):
        arr[i][j] += plus

for i in range(M):
    for j in range(M):
        print(arr[i][j] + 1, end=" ")
    print()

# 시간 초과 코드: 매 날짜 마다 모든 애벌레 갱신
# for date in grow:
#     # 1. 왼쪽 / 오른쪽 열에 있는 애벌레 자라기
#     for i in range(M-1, -1, -1):  # 맨 왼쪽 열
#         arr[i][0][0] += date[M - i - 1]
#         arr[i][0][1] = date[M - i - 1]
#
#     for i in range(1, M):     # 맨 위쪽 행
#         arr[0][i][0] += date[M + i - 1]
#         arr[0][i][1] = date[M + i - 1]
#
#     # 2. 나머지 애벌레 자라기(1, 1 부터 시작)
#     for i in range(1, M):
#         for j in range(1, M):
#             max_grow = 0
#             for k in range(3):
#                 nx, ny = i + dx[k], j + dy[k]
#                 max_grow = max(max_grow, arr[nx][ny][1])
#             arr[i][j][0] += max_grow
#             arr[i][j][1] = max_grow
#

