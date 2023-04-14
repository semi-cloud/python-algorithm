# 특정 지점으로 부터 수색 범위 내에 존재하는 노드에서 먹을 수 있는 아이템 개수의 최대값
from heapq import heappush, heappop

def floyd_warshall():  # O(N^3)
    for i in range(1, n+1):
        dist[i][i] = 0  # 자기 자신은 0

    # 2. 노드 하나씩 거친는 경우를 가정하고 비용 갱신
    for k in range(1, n+1):  # 거치는 점
        for i in range(1, n+1):  # 시작점
            for j in range(1, n+1):  # 끝점
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

# 1. 최단 거리 업데이트  O(ELogV)
n, m, r = map(int, input().split())
items = [-1] + list(map(int, input().split()))
dist = [[int(1e9) for _ in range(n+1)] for _ in range(n+1)]
ans = 0

for i in range(r):
    a, b, d = map(int, input().split())
    dist[a][b] = d      # 이웃 노드 거리 한번에 초기화
    dist[b][a] = d

floyd_warshall()
# 2. 그래프 탐색하면서 갈 수 있다면 아이템 얻기(각 노드 마다 구해서 최대값 찾기)
for i in range(1, n+1):
    temp = 0
    for j in range(1, n+1):
        d = dist[i][j]
        if d <= m:  # 수색 범위 내라면 갈 수 있으므로 아이템 먹기
            temp += items[j]
    ans = max(ans, temp)
print(ans)


# 특정 지점만 해주는게 아니고 모든 지점 => 모든 지점으로 가는 경우의 수 체크
# 다익스트라 여러 번 돌리기(시간 초과 날 것 같으면 비용 공유가 가능한 경우 시작 큐에 동시에 추가하고 시작)/ 플로이드 워샬
# def dijkstra(start):
#     dist = [int(1e9) for _ in range(n + 1)]
#     q = []
#     heappush(q, (0, start))
#     dist[start] = 0
#
#     # 현재 노드에서 가장 짧은 거리에 있는 노드를 택
#     while q:
#         cur_d, cur_v = heappop(q)
#         if cur_d > dist[cur_v]:  # 중복 방문 체크
#             continue
#
#         for next_v, next_d in graph[cur_v]:    # 해당 노드 이웃 들의 최단 거리 업데이트
#             # 해당 노드를 거쳐가는 경우의 수와 기존에 계산 했던 짧은 거리를 비교 후, 더 짧은 경로로 업데이트
#             new_cost = next_d + dist[cur_v]
#             if dist[next_v] > new_cost:
#                 dist[next_v] = new_cost
#                 q.append((new_cost, next_v))  # 갱신된 경우 큐에 추가
