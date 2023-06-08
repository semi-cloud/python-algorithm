# 1번섬에 구명 보트 존재, 최대한 많은 수의 양들을 1번 섬으로 도착시키기

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

# 원래 잡아 먹은 만큼 늑대 개수 감소시켜야함(최대 한 마리 양만 잡기 가능)
# 현재 줄기당 한번만 지나가므로 늑대 개수 조절 필요 X(다시 방문하는 일 X)
def dfs(v):
    sheep_cnt = 0
    for node in graph[v]:    # 리프 노드로 내려가기 : 2 5 7 6 3 4
        sheep_cnt += dfs(node)   # 다시 올라오면서 구출 가능한 양 개수 저장

    sheep_cnt += info[v]
    if sheep_cnt < 0:   # 현재 늑대 노드 + 올라온 양 개수보다 늑대 수가 많은 경우
        sheep_cnt = 0
    return sheep_cnt

N = int(input())
info = [0, 0]
graph = [list() for _ in range(N+1)]
res = 0

for i in range(2, N+1):
    a, b, c = list(input().split())
    if a == "W":
        info.append(-int(b))    # 양 개체수는 양수, 늑대 개체수는 음수로 저장
    else:
        info.append(int(b))
    graph[int(c)].append(i)     # 아래 방향으로 탐색할 수 있도록

print(dfs(1))  # 그래프 탐색 한번으로 끝내기


# for sheep in sheeps:    # 시간 초과 부분
#     res += dfs(sheep)   # 1번 노드로 도착한 양 개수 반환
# while st:
# v = st.pop()
# if v == 1:    # 1번 노드로 도착 시 남아있는 양 개수 반환
#     return cur_sheep
#
# if cur_sheep <= 0:
#     return 0
#
# type, cnt, parent = graph[v]
# if type == "W":  # 부모 노드가 늑대인 경우
#     if cur_sheep > cnt:  # 잡아 먹은 만큼 늑대 개수 감소시키기(최대 한 마리 양만 잡기 가능)
#         graph[v][1] = 0
#     else:
#         graph[v][1] -= cur_sheep
#     st.append([parent, cur_sheep - cnt])
# else:
#     st.append([parent, cur_sheep])


