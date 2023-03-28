# 인식 가능한 점을 통해 만들 수 있는 총 패턴의 개수 구하기
# 각 점마다 만들 수 있는 패턴, 모양이 같아도 방향이 다르면 다름
# 순열 구하는 거랑 비슷 (1 -> 2 -> 3 / 3 -> 2 -> 1 / 1 -> 3 -> 2)

dx, dy = [0, 0, 1, -1, -1, 1, -1, 1], [1, -1, 0, 0, -1, 1, 1, -1]
def bt(x, y, depth, target, phone, visited):  # 백트래킹으로 방문했던 지점 다시 릴리즈 => 재귀 depth 타겟 만큼 되면 종료
    global ans
    if depth == target:
        ans += 1
        return

    for i in range(8):  # 1 인 지점으로 상하좌우 이동
        nx, ny = x + dx[i], y + dy[i]
        if 0 > nx or nx >= 4 or 0 > ny or ny >= 3:
            continue

        if not visited[nx][ny] and phone[nx][ny] == 1:
            visited[nx][ny] = True
            bt(nx, ny, depth + 1, target, phone, visited)
            visited[nx][ny] = False

ans = 0
def solution(phone):
    global ans

    total = 0
    for i in range(4):
        for j in range(3):
            if phone[i][j] == 1:
                total += 1

    for cnt in range(2, total + 1):  # 인식 가능한 점이 i개 일 때 만들 수 있는 패턴 개수(2개 이상)
        for i in range(4):
            for j in range(3):
                if phone[i][j] == 1:
                    visited = [[False for _ in range(3)] for _ in range(4)]
                    visited[i][j] = True
                    bt(i, j, 1, cnt, phone, visited)  # (i, j) 에서 cnt 개의 패턴 인식 수
    return ans

print(solution([[0, 1, 0], [1, 1, 1], [1, 0, 0], [0, 0, 1]]))  # 96
print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]))  # 193912
print(solution([[1, 1, 0], [0, 1, 0], [0, 0, 0], [0, 0, 0]]))  # 12

# DFS 를 활용해 방문 배열에 방향 까지 체크 하면 맨 처음 시작하는 노드의 방문 방향 체크가 불가능(다음 노드의 어느 방향으로 들어왔느냐를 체크 하기 때문에)
# visited = [[[False for _ in range(8)] for _ in range(3)] for _ in range(4)]
# if phone[i][j] == 1:
# for k in range(8):  # 시작 지점에서 해당 방향으로 갔을 때 방문 처리
#     bt(i, j, k, cnt, phone, visited)   # (i, j) 에서 cnt 개의 패턴 인식 수

# def dfs(a, b, start, target, phone, visited):
#     st = list()
#     st.append((a, b, start, 1))  # 위치, 점 개수
#     temp = 0
#
#     while st:
#         x, y, dir, cnt = st.pop()
#         print(x, y, dir, cnt)
#         if cnt == target:  # 2(해당 패턴에서의 탐색은 종료)
#             temp += 1
#             continue
#
#         for i in range(8):  # 1 인 지점으로 상하좌우 이동
#             nx, ny = x + dx[i], y + dy[i]
#             if 0 > nx or nx >= 4 or 0 > ny or ny >= 3:
#                 continue
#
#             if not visited[nx][ny][i] and phone[nx][ny] == 1:
#                 visited[nx][ny][i] = True
#                 st.append((nx, ny, i, cnt + 1))
#     return temp


