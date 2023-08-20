# 완전 탐색: 종이를 적절히 잘라서 조각의 합을 최대로 얻기
# 내가 헷갈린 부분은 이중 포문으로 비어있는 곳을 찾는 방식으로 안하고 조각이 끝나는 지점부터 다시 탐색하는 방향으로 하면 전체 공간을 다 돌수가 있나?>
# 1. visit[i][j] = True  # 무조건 복사를 하고 나서 진행, 아니면 재귀 전에 배열 넘겨준거까지 영향이 가버림

import sys
sys.setrecursionlimit(10000)

def calculate(x, y, nx, ny):
    decimal = 0
    num = arr[x][y]
    for i in range(x + 1, nx + 1):    # 세로 조각인 경우
        num += arr[i][y]

    for j in range(y + 1, ny + 1):    # 가로 조각인 경우
        num += arr[x][j]

    for i in range(len(num)):
        decimal += int(num[i]) * (10 ** (len(num)-1-i))
    return decimal

def check_visited(x, y, nx, ny):  # 조각의 모든 지점 방문 체크
    for i in range(x, nx + 1):
        if visit[i][y]: return True

    for j in range(y, ny + 1):
        if visit[x][j]: return True

    return False

def reverse_visit(x, y, nx, ny, flag):   # 해당 조각의 모든 지점 방문 여부 뒤집기
    for i in range(x, nx + 1):
        visit[i][y] = flag

    for j in range(y, ny + 1):
        visit[x][j] = flag

dx, dy = [0, 0, 0, 0, 1, 2, 3], [0, 1, 2, 3, 0, 0, 0]  # 가로 방향, 세로 방향의 모든 선택지(따로 나눠서 재귀 돌리는게 X)
def bt(idx, sum):
    global res

    if idx == N * M:       # 모든 배열을 방문했다면 최대값 갱신
        res = max(res, sum)  # 더 이상 방문할 곳이 없는 경우, 그리고 여기다 하면 방문 처리 해제된 이후에 로직도 들어오네
        return

    x, y = idx // M, idx % M   # 증가 숫자로 위치 인덱스 찾기(이중 포문 X)
    # if x < 0 or x >= N or y < 0 or y >= M: return

    if visit[x][y]:        # 만약 바로 다음에 갈 곳이 방문 되어 있어도, 방문 안된 곳이 나올때 까지 idx 값을 계속 증가시켜가면서 탐색 해야함(중요)
        bt(idx + 1, sum)

    for i in range(7):         # 가능한 모든 조각 탐색
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M or check_visited(x, y, nx, ny): continue

        reverse_visit(x, y, nx, ny, True)   # 방문 처리
        bt(idx + 1, sum + calculate(x, y, nx, ny))
        reverse_visit(x, y, nx, ny, False)  # 재귀 이후 방문 처리 해제

    # res = max(res, sum)  # 해당 지점에서 갱신해도 되는데 인덱스 에러 안나게 범위 체크 필요

N, M = map(int, input().split(" "))
arr = [input() for _ in range(N)]
visit = [[False for _ in range(M)] for _ in range(N)]
res = 0
bt(0, 0)
print(res)


# 1. 매번 배열을 탐색하면서 방문하지 않은 곳을 탐색 시작 위치로 지정하는 방식 : X
# for x in range(N):
#     for y in range(M):      # 해당 방식은 무한 루프를 돔([x][y] 위치에서 안되서 그 전 호출했던 위치로 돌아가야 하는데 그 이후 [x][y+1] 위치에서 또 다시 탐색을 시작하기 떄문에)

# 2. 가로 세로 따로 나눠서 재귀 돌리는 방식 : X
# visited = [v[:] for v in visit]
# for k in range(max_piece):   # 각 조각 개수
#     for _ in range(k):
#         nx, ny = nx, ny + 1   # 1. 가로 방향
#         if nx < 0 or nx >= N or ny < 0 or ny >= M or visited[nx][ny]:
#             return
#         visited[nx][ny] = True
#         temp += arr[nx][ny]
#     else:
#         bt(visited, sum + calculate(temp))
#
#    temp = arr[i][j]
#    visited = [v[:] for v in visit]
#    visited[i][j] = True
#    nx, ny = i, j
#    for k in range(max_piece):  # 각 조각 개수
#        for _ in range(k):
#             nx, ny = nx + 1, ny  # 2. 세로 방향
#             if nx < 0 or nx >= N or ny < 0 or ny >= M or visited[nx][ny]:
#                 return
#             visited[nx][ny] = True
#             temp += arr[nx][ny]
#        else:
#           bt(visited, sum + calculate(temp))
