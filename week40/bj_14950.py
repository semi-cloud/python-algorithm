# 정복하려는 노드 A와 연결되어 있는 B도 정복시켜야 함, 도로 비용만큼 비용 소모, 모든 도로 비용이 t만큼 증가
# 각 도시를 정복할 때, 연결되어 있는 도시들 중에서 정복(방문)되어 있고 가장 적은 간선 비용을 가진 도시 택 = 최소
# 다익스트라가 아니고, 그냥 최소 스패닝 트리(가장 최소 간선으로 모든 노드 정복하기)


# 무조건 간선이 작은 것부터 처리해도, 둘 중 하나가 정복이 되어야 한다는 조건을 걸때랑 값이 같음

def find_parent(x):
    if x == parent[x]:
        return parent[x]

    parent[x] = find_parent(parent[x])
    return parent[x]

def union(a, b):
    pa = find_parent(a)
    pb = find_parent(b)

    if pa < pb:
        parent[pb] = pa   # 작은거를 대입하도록
    else:
        parent[pa] = pb

def kruskal():
    turn, res = 0, 0

    for cost, x, y in edges:
        if find_parent(x) == find_parent(y):   # 사이클 방지(이미 연결되어 있는 경우)
            continue

        union(x, y)
        res += cost + t * turn  # 정복하고 소모 비용 증가
        turn += 1             # 정복된 후에는 비용이 증가
    return res

N, M, t = map(int, input().split(" "))   # 10000, 30000
visit = [False for _ in range(N+1)]
edges = list()
parent = [0] + [i+1 for i in range(N)]

for i in range(M):
    a, b, c = map(int, input().split(" "))
    edges.append((c, a, b))

edges.sort(key=lambda x: x[0])

print(kruskal())

# 해당 방식이 안되는 이유
# 제일 최근에 정복한 노드에 인접한 노드에서 최소값을 찾고 그 노드를 정복 하려고 하는데, 더 작은 비용의 간선이 존재할 수 있음
# 4 정복 -> 인접한 2 정복 : 비용 4 VS 다시 3에서 인접한 2 정복 : 비용 2

# from heapq import heappush, heappop
#
# def bfs(v):
#     global res
#
#     st = [(v, 0)]
#     visit[v] = True
#     conquest = 0
#
#     while st:
#         hq = []
#         n, dist = st.pop()      # 이미 정복이 된 도시
#         res += dist
#
#         for node, cost in graph[n]:  # 이웃 도시 검사해서 큐에 추가
#             if visit[node]:
#                 continue  # 이미 정복된 도시는 패스
#             heappush(hq, (cost, node))
#
#         if hq:         # 이웃 노드가 존재하는 경우
#             min_cost, min_node = heappop(hq)  # 이웃 노드 중에 가장 짧은 비용 가진 도시 택
#             visit[min_node] = True           # 도시 정복 하기
#             new_cost = min_cost + t * conquest   # 이전에 정복된 횟수 만큼 도로 비용 증가 해서 거리 계산
#
#             conquest += 1       # 정복 횟수 증가
#             st.append((min_node, new_cost))

# if q:
#     if visit[q[0][0]] or visit[q[0][1]]:    # 대기열에 있는 도로 중에서 정복할 수 있는 도로가 존재하면
#         union(q[0][0], q[0][1])             # 정복
#         res += cost + t * turn
#         visit[x] = True
#         visit[y] = True
#         turn += 1
#
# if visit[x] or visit[y]:  # 둘 중 하나 노드 라도 정복이 된 경우
#     union(x, y)
#     res += cost + t * turn            # 정복하고 소모 비용 증가
#     visit[x] = True
#     visit[y] = True
# else:                   # 두 노드가 모두 정복 되어 있지 않다면 정복 불가능
#     q.append((x, y, cost))     # 대기열에 추가
