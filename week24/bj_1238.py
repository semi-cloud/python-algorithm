# N명의 학생들 중 X번째 집을 오고 가는데 가장 오래 걸리는 학생의 소요시간 구하기
# 모든 집마다 파티장까지 Dijkstra 돌리는 게 아니라,
# 간선 방향을 다 반대로 뒤집은 다음에 파티장에서 Dijkstra 1번만 돌리기

import sys
from collections import defaultdict
import heapq        # 우선 순위 큐

def dijkstra(start, graph):  # O(ELogE)
    # X 로부터 오는 경로의 최소값
    dp = [int(1e9)] * (N + 1)  # 무한대로 초기화
    dp[start] = 0
    q = []
    heapq.heappush(q, (0, start))   # 거리 순으로 최소 힙 생성

    while q:   # O(N*ELogE)
        dist, cur = q.pop()   # 가장 짧은 거리의 노드를 (LogN의 시간에 꺼내기)
        if dist > dp[cur]:    # 이미 최단 비용이 정해진 노드라면 패스(방문 처리)
            continue

        for node_index, node_cost in graph[cur]:  # 가장 최단 거리 노드의 인접한 노드 검사
            new_cost = dist + node_cost

            if dp[node_index] > new_cost:  # 비용이 더 작다면 갱신
                dp[node_index] = new_cost
                heapq.heappush(q, (new_cost, node_index))  # 거리 값이 갱신된 최단 거리 노드만 우선순위 큐에 추가
    return dp

input = sys.stdin.readline
N, M, X = map(int, input().split())
graph_origin = defaultdict(list)
graph_inverse = defaultdict(list)
result = 0

for _ in range(M):
    s, e, d = map(int, input().split())
    graph_origin[s].append((e, d))    # 정방향 그래프 : X -> 특정 노드 1 -> 3 (x) 2
    graph_inverse[e].append((s, d))   # 역방향 그래프 : 특정 노드 -> X   3 -> 1 (2)

dp_down = dijkstra(X, graph_origin)
dp_up = dijkstra(X, graph_inverse)

for i in range(1, N+1):
    result = max(result, dp_up[i] + dp_down[i])
print(result)

# 힙을 사용 했지만 시간 초과가 난 풀이 : O(N*M*logM) => default-dict 문제(일반 딕셔너리보다 느림)
# A -> X
# for i in range(1, N+1):
#     if i == X:
#         continue
#     dist_up = dijkstra(i)
#     total_sum = dist_up[X] + dist_down[i]
#     if result < total_sum:
#         result = total_sum
# print(result)

# 리스트 컨프리 헨션 사용한 풀이 : 속도는 더 빠름
# dist_down = dijkstra(X, graph_origin)
# result = [dijkstra(i, graph_origin)[X] + dist_down[i] for i in range(1, N+1)]
# print(result)

# O(N^2) 풀이
# visited = [False] * (N + 1)  # 방문 배열
# def get_smallest_dist():   # 방문하지 않은 노드 중에 가장 최단 거리 노드 찾기
#     min_val = float("inf")
#     min_index = 0
#     for i in range(1, N+1):
#         if dp[i] < min_val and not visited[i]:
#             min_val = dp[i]
#             min_index = i
#     return min_index
#
# def dijkstra():
#     dp[X] = 0   # 자기 자신에 대한 최단 거리는 0
#     visited[X] = True
#     for adj in dist_info[X]:    # 노드 X 에서 시작, 인접 정보 초기화
#         dp[adj[0]] = adj[1]
#
#     for i in range(N-1):   # 시작 노드를 제외한 N-1 노드에 대해 반복
#         cur = get_smallest_dist()
#         visited[cur] = True
#
#         for adj in dist_info[cur]:  # 가장 최단 경로 노드의 인접한 노드들을 검사 (인접 노드, 비용)
#             new_cost = dp[cur] + adj[1]
#             if dp[adj[0]] > new_cost:    # 자신을 거쳐 가는 것이 빠른지 기존에 최단 거리가 더 짧은지 비교 후 거리 갱신
#                 dp[adj[0]] = new_cost
#     print(dp)
