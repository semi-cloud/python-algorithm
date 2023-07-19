# 백트래킹 / DFS로 하면 깊이가 너무 깊어져서 시간 초과
# BFS로 한 뎁스마다 모두 값 확인하면서 가야 바로 최소값 찾을 수 있음
# 한 자리씩(1의 자리(depth 1) -> 10의 자리(depth 2) ...) 버려가면서 버튼 택

from collections import deque
import math

def bfs(n):
    res = float("inf")
    q = deque([[n, 1, 0]])

    while q:
        cur_floor, depth, cnt = q.popleft()

        if cnt >= res: continue  # 최소값 보다 커지면 종료
        if cur_floor == 0:
            res = min(res, cnt)
            continue

        offset = 10 ** depth        # 10
        cur = (0.1 ** depth) * cur_floor  # 1.6
        down_floor = math.floor(cur) * offset  # 10
        up_floor = math.ceil(cur) * offset     # 20

        q.append([down_floor, depth + 1, cnt + ((cur_floor - down_floor) / (offset * 0.1))])  # -X 자리 버리기
        q.append([up_floor, depth + 1, cnt + ((up_floor - cur_floor) / (offset * 0.1))])  # +X 자리 올리기

    return res

def solution(storey):  # 100,000,000, 현재 층수
    return bfs(storey)


# 2. 백트래킹(재귀) 풀이
# 가능한 버튼 목록을 미리 만들어두고 하나씩 선택해보는 방식(비효율적)
# def bt(n, depth, buttons, visited):
#     if depth >= res: return   # 최소값보다 커지면 종료
#
#     if n == 0:
#         res = min(res, depth)
#         return
#
#     for i in range(len(buttons)):
#         new_floor = n + buttons[i]
#         if visited[new_floor] or new_floor < 0: continue  # 방문했거나 0보다 작은 경우 탐색 X
#
#         print(depth, buttons[i], new_floor, res)
#
#         visited[new_floor] = True
#         bt(new_floor, depth + 1, buttons, visited)
#         visited[new_floor] = False
