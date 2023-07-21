# 중심이 되는 칸 : 강도 X 2, 여러 부메랑들의 강도 합의 최대값 찾기
# 조각을 어떻게 내느냐에 따라서 만들 수 있는 부메랑 개수가 달라짐

def dfs(x, y, total, visit):  # 해당 위치를 중심으로 여러 가지 부메랑이 가능
    global res

    if y == M:    # 인덱스 2차원 배열에 맞춰서 수정
        x += 1
        y %= M

    if x == N:   # 끝에 다다르면 최대값 계산(범위를 벗어나면)
        res = max(res, total)   # 모든 공간을 커버하지 못할 수 있음
        return

    if not visit[x][y]:
        for a, b, c, d in boomerang:
            nx, ny, xx, yy = x + a, y + b, x + c, y + d

            if 0 <= nx < N and 0 <= xx < N and 0 <= ny < M and 0 <= yy < M and not visit[nx][ny] and not visit[xx][yy]:  # 만들 수 있는 부메랑
                visit[x][y], visit[nx][ny], visit[xx][yy] = True, True, True
                sum = strength[nx][ny] + strength[xx][yy]
                dfs(x, y + 1, total + sum + strength[x][y] * 2, visit)
                visit[x][y], visit[nx][ny], visit[xx][yy] = False, False, False

    dfs(x, y + 1, total, visit)


N, M = map(int, input().split(" "))
strength = [list(map(int, input().split(" "))) for _ in range(N)]  # 강도
boomerang = [[0, -1, 1, 0], [-1, 0, 0, -1], [-1, 0, 0, 1], [1, 0, 0, 1]]   # 부메랑 모양 (0,0 기준은 가운데)
res = 0

if N < 2 or M < 2:   # 재료 크기가 작아서 부메랑 만들 수 없는 경우
    print(0)
else:
    dfs(0, 0, 0, [[False for _ in range(M)] for _ in range(N)])
    print(res)


# 시간 초과 : 매 재귀 마다 배열 완전 탐색
# def dfs(x, y, total, visit):  # 해당 위치를 중심으로 여러 가지 부메랑이 가능
#     global res
#
#     # visit = [v[:] for v in visit]  # 딥 카피 : 하니까 에러
#     for x in range(N):       # 5 * 5
#         for y in range(M):   # 각 위치가 부메랑의 중심
#
#             if depth == 0:
#                 visit = [[False for _ in range(M)] for _ in range(N)]  # 방문 배열 초기화
#
#             for b in boomerang:  # 만들 수 있는 부메랑
#                 temp = []
#                 for i in range(2):
#                     nx, ny = x + b[i][0], y + b[i][1]
#                     if nx < 0 or nx >= N or ny < 0 or ny >= M or visit[nx][ny]:  # 부메랑을 만들 수 없는 경우
#                         break
#                     temp.append([nx, ny])
#                 else:               # 부메랑을 만들 수 있는 경우
#                     visit[x][y] = True
#                     sum = 0
#                     for t in temp:
#                         visit[t[0]][t[1]] = True
#                         sum += strength[t[0]][t[1]]
#
#                     dfs(x, y + 1, total + sum + strength[x][y] * 2, visit)
#
#                     for t in temp:
#                         visit[t[0]][t[1]] = False   # 방문 해제
#
# N, M = map(int, input().split(" "))
# strength = [list(map(int, input().split(" "))) for _ in range(N)]  # 강도
# boomerang = [[[0, -1], [1, 0]], [[-1, 0], [0, -1]], [[-1, 0], [0, 1]], [[1, 0], [0, 1]]]   # 부메랑 모양 (0,0 기준은 가운데)
# res = 0